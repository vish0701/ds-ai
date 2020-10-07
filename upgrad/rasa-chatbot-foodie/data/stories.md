### Happy path < 300 #1
* greet
    - utter_greet
* restaurant_search
    - utter_ask_location
* restaurant_search{"location": "delhi"}
    - slot{"location": "delhi"}
    - action_check_location
    - slot{"location": "delhi"}
    - slot{"location_found": "found"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "chinese"}
    - slot{"cuisine": "chinese"}
    - utter_ask_price
* restaurant_search{"price": "less than 300"}
    - slot{"price": "less than 300"}
    - utter_search_msg
    - action_restaurant
    - slot{"rest_found": "yes"}  
    - utter_ask_mail
* affirm{"email": "mondal.arup@gmail.com"}
    - slot{"email": "mondal.arup@gmail.com"}
    - email_restaurant_details

### Happy path < 300 #2
* greet
    - utter_greet
* restaurant_search
    - utter_ask_location
* restaurant_search{"location": "bengaluru"}
    - slot{"location": "bengaluru"}
    - action_check_location
    - slot{"location": "bengaluru"}
    - slot{"location_found": "found"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "italian"}
    - slot{"cuisine": "italian"}
    - utter_ask_price
* restaurant_search{"price": "less than 300"}
    - slot{"price": "less than 300"}
    - utter_search_msg
    - action_restaurant
    - slot{"rest_found": "yes"}
    - utter_ask_mail
* affirm{"email": "vishiyer0701@gmail.com"}
    - slot{"email": "vishiyer0701@gmail.com"}
    - email_restaurant_details

### Happy path < 300 #3
* greet
    - utter_greet
* restaurant_search
    - utter_ask_location
* restaurant_search{"location": "bengaluru"}
    - slot{"location": "bengaluru"}
    - action_check_location
    - slot{"location": "bengaluru"}
    - slot{"location_found": "found"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "american"}
    - slot{"cuisine": "american"}
    - utter_ask_price
* restaurant_search{"price": "less than 300"}
    - slot{"price": "less than 300"}
    - utter_search_msg
    - action_restaurant
    - slot{"rest_found": "yes"}
    - utter_ask_mail
* affirm{"email": "vishiyer0701@gmail.com"}
    - slot{"email": "vishiyer0701@gmail.com"}
    - email_restaurant_details

### Happy path < 300 #4
* greet
    - utter_greet
* restaurant_search
    - utter_ask_location
* restaurant_search{"location": "coimbatore"}
    - slot{"location": "coimbatore"}
    - action_check_location
    - slot{"location": "coimbatore"}
    - slot{"location_found": "found"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "mexican"}
    - slot{"cuisine": "mexican"}
    - utter_ask_price
* restaurant_search{"price": "less than 300"}
    - slot{"price": "less than 300"}
    - utter_search_msg
    - action_restaurant
    - slot{"rest_found": "yes"}
    - utter_ask_mail
* affirm{"email": "kousikdas05@gmail.com"}
    - slot{"email": "kousikdas05@gmail.com"}
    - email_restaurant_details


### Happy path < 300 #5
* greet
    - utter_greet
* restaurant_search
    - utter_ask_location
* restaurant_search{"location": "nagpur"}
    - slot{"location": "nagpur"}
    - action_check_location
    - slot{"location": "nagpur"}
    - slot{"location_found": "found"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "italian"}
    - slot{"cuisine": "italian"}
    - utter_ask_price
* restaurant_search{"price": "less than 300"}
    - slot{"price": "less than 300"}
    - utter_search_msg
    - action_restaurant
    - slot{"rest_found": "yes"}
    - utter_ask_mail
* affirm{"email": "kiranck@gmail.com"}
    - slot{"email": "kiranck@gmail.com"}
    - email_restaurant_details



### Story 2: Happy path 300-700
* greet
    - utter_greet
* restaurant_search
    - utter_ask_location
* restaurant_search{"location": "delhi"}
    - slot{"location": "delhi"}
    - action_check_location
    - slot{"location": "delhi"}
    - slot{"location_found": "found"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "chinese"}
    - slot{"cuisine": "chinese"}
    - utter_ask_price
* restaurant_search{"price": "between 300 and 700"}
    - slot{"price": "between 300 and 700"}
    - utter_search_msg
    - action_restaurant
    - slot{"rest_found": "yes"}
    - utter_ask_mail
* affirm{"email": "vishiyer0701@gmail.com"}
    - slot{"email": "vishiyer0701@gmail.com"}
    - email_restaurant_details


# Story 3: Happy path > 700
* greet
    - utter_greet
* restaurant_search
    - utter_ask_location
* restaurant_search{"location": "delhi"}
    - slot{"location": "delhi"}
    - action_check_location
    - slot{"location": "delhi"}
    - slot{"location_found": "found"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "chinese"}
    - slot{"cuisine": "chinese"}
    - utter_ask_price
* restaurant_search{"price": "more than 700"}
    - slot{"price": "more than 700"}
    - utter_search_msg
    - action_restaurant
    - slot{"rest_found": "yes"}
    - utter_ask_mail
* affirm{"email": "vishiyer0701@gmail.com"}
   - slot{"email": "vishiyer0701@gmail.com"}
    - email_restaurant_details


## Story 4: No email < 300
* greet
    - utter_greet
* restaurant_search
    - utter_ask_location
* restaurant_search{"location": "delhi"}
    - slot{"location": "delhi"}
    - action_check_location
    - slot{"location": "delhi"}
    - slot{"location_found": "found"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "chinese"}
    - slot{"cuisine": "chinese"}
    - utter_ask_price
* restaurant_search{"price": "less than 300"}
    - slot{"price": "less than 300"}
    - utter_search_msg
    - action_restaurant
    - slot{"rest_found": "yes"}
    - utter_ask_mail
* deny
    - utter_bye_final

## Story 5: No email 300-700
* greet
    - utter_greet
* restaurant_search
    - utter_ask_location
* restaurant_search{"location": "delhi"}
    - slot{"location": "delhi"}
    - action_check_location
    - slot{"location": "delhi"}
    - slot{"location_found": "found"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "chinese"}
    - slot{"cuisine": "chinese"}
    - utter_ask_price
* restaurant_search{"price": "between 300 and 700"}
    - slot{"price": "between 300 and 700"}
    - utter_search_msg
    - action_restaurant
    - slot{"rest_found": "yes"}
    - utter_ask_mail
* deny
    - utter_bye_final

## Story 6: No email > 700
* greet
    - utter_greet
* restaurant_search
    - utter_ask_location
* restaurant_search{"location": "delhi"}
    - slot{"location": "delhi"}
    - action_check_location
    - slot{"location": "delhi"}
    - slot{"location_found": "found"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "chinese"}
    - slot{"cuisine": "chinese"}
    - utter_ask_price
* restaurant_search{"price": "more than 700"}
    - slot{"price": "more than 700"}
    - utter_search_msg
    - action_restaurant
    - slot{"rest_found": "yes"}
    - utter_ask_mail
* deny
    - utter_bye_final


## Story 7: Location not found
* greet
    - utter_greet
* restaurant_search
    - utter_ask_location
* restaurant_search{"location": "mbusmkwoid"}
    - slot{"location": "mbusmkwoid"}
    - action_check_location
    - slot{"location": null}
    - slot{"location_found": "notfound"}
    - utter_location_notfound
* restaurant_search{"location": "bangalore"}
    - slot{"location": "bangalore"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "italian"}
    - slot{"cuisine": "italian"}
    - utter_ask_price
* restaurant_search{"price": "less than 300"}
    - slot{"price": "less than 300"}
    - utter_search_msg
    - action_restaurant
    - slot{"rest_found": "yes"}
    - utter_ask_mail 
* affirm{"email": "vishiyer0701@gmail.com"}
    - slot{"email": "vishiyer0701@gmail.com"}
    - email_restaurant_details


## Story 9: Hi and Bye
* greet
    - utter_greet
* goodbye
    - utter_bye_noop

## Story: Restaurant not found (simple) - < 300
* greet
    - utter_greet
* restaurant_search
    - utter_ask_location
* restaurant_search{"location": "bangalore"}
    - slot{"location": "bangalore"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "italian"}
    - slot{"cuisine": "italian"}
    - utter_ask_price
* restaurant_search{"price": "less than 300"}
    - slot{"price": "less than 300"}
    - utter_search_msg
    - action_restaurant
    - slot{"rest_found": "no"}
    - utter_bye_notfound
    