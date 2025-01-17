from __future__ import absolute_import
from __future__ import division
from __future__ import unicode_literals

# from rasa_core.actions.action import Action
from rasa_core_sdk import Action
from rasa_core_sdk.events import SlotSet

# from rasa_core.events import SlotSet
import json
#from send_mail import email
from zomato_slots import results
from city_check import check_location
from email_config import Config
from flask_mail_check import send_email

class ActionSearchRestaurants(Action):
    def name(self):
        return 'action_restaurant'
        
    def run(self, dispatcher, tracker, domain):
        loc = tracker.get_slot('location')
        cuisine = tracker.get_slot('cuisine')
        price = tracker.get_slot('price')
        
        global restaurants


        restaurants = results(loc, cuisine, price)
        top5 = restaurants.head(5) 
        
        # top 5 results to display
        
        if len(top5)>0: 
            rest_found = 'yes'
            response = 'Showing you top results:\n\n' 
            i = 1
            for index, row in top5.iterrows():
                response = response + str(i) + '. ' + str(row["restaurant_name"]) + ' (rated ' + row['restaurant_rating'] + ') in ' + row['restaurant_address'] + ' and the average budget for two people ' + str(row['budget_for2people'])+"\n"
                i += 1  
        else:
            rest_found = 'no'
            response = 'Sorry, no restaurants found matching your crtieria.'

#        response = response + '. rest_found:' + rest_found

        dispatcher.utter_message(str(response))
        return [SlotSet("rest_found", rest_found)]


class SendMail(Action):
    def name(self):
        return 'email_restaurant_details'
        
    def run(self, dispatcher, tracker, domain):
        recipient = tracker.get_slot('email')

        top5 = restaurants.head(5)
        print("got this email id {}".format(recipient))
        send_email(recipient, top5)

        dispatcher.utter_message("Details of the top 5 restuarants have been emailed.")


class Check_location(Action):
    def name(self):
        return 'action_check_location'
        
    def run(self, dispatcher, tracker, domain):
        loc = tracker.get_slot('location')
        check = check_location(loc)
        
        return [SlotSet('location',check['location_new']), SlotSet('location_found',check['location_f'])]
        
       
