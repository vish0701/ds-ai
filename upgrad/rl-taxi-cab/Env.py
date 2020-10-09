# Import routines

import numpy as np
import math
import random
from itertools import permutations

# Defining hyperparameters
m = 5 # number of cities, ranges from 1 ..... m
t = 24 # number of hours, ranges from 0 .... t-1
d = 7  # number of days, ranges from 0 ... d-1
C = 5 # Per hour fuel and other costs
R = 9 # per hour revenue from a passenger
lambda_loc={0:2,1:12,2:4,3:7,4:8}

class CabDriver():

    def __init__(self):
        """initialise your state and define your action space and state space"""
        self.action_space = [(0, 0)] + list(permutations([i for i in range(m)], 2))
        self.state_space = [[x,y,z] for x in range(m) for y in range(t) for z in range(d)]
        self.state_init =random.choice(self.state_space) 

        # Start the first round
        self.reset()


    ## Encoding state (or state-action) for NN input

    def state_encod_arch1(self, state):
        """convert the state into a vector so that it can be fed to the NN. This method converts a given sta
        te into a vector format. Hint: The vector is of size m + t + d."""
        state_encod = list(np.zeros(m+t+d))
        current_loc,curr_time,curr_day=self.getstate_currstate_currloc_time_day(state)
        state_encod[current_loc] = 1
        state_encod[m+curr_time] = 1
        state_encod[m+t+curr_day] = 1

        return state_encod


    # Use this function if you are using architecture-2 
    def state_encod_arch2(self, state, action):
        """convert the (state-action) into a vector so that it can be fed to the NN. This method converts a given state-action pair into a vector format. Hint: The vector is of size m + t + d + m + m."""
        state_encod=list(np.zeros(3*m+t+d))
        current_loc,curr_time,curr_day=self.getstate_currstate_currloc_time_day(state)
        pickup_loc,drop_loc=self.getaction_pickup_drop_loc(action)
        state_encod[current_loc]=1
        state_encod[m+curr_time]=1
        state_encod[m+t+curr_day]=1
        state_encod[m+t+d+pickup_loc]=1
        state_encod[2*m+t+d+drop_loc]=1 
        
        return state_encod


    # Getting number of requests

    def requests(self, state):
        """Determining the number of requests basis the location. 
        Use the table specified in the MDP and complete for rest of the locations"""
        location = state[0]

        #reading values from dictionery initilized
        requests = np.random.poisson(lambda_loc[location])

        if requests > 15:
            requests = 15
        # (0,0) is not considered as customer request
        #but the driver may reject the ride by taking action (0,0)
        possible_actions_index = random.sample(range(1, (m-1)*m + 1), requests) + [0]
        actions = [self.action_space[i] for i in possible_actions_index]

        return possible_actions_index,actions   



    def reward_func(self, wait_time, transit_time, ride_time):
        """Takes in state, action and Time-matrix and returns the reward"""        
        reward = (R * ride_time) - (C * (ride_time + wait_time + transit_time))
        return reward




    def next_state_func(self, state, action, Time_matrix):
        """Takes state and action as input and returns next state"""
        # Initialize various times
        total_time   = 0
        transit_time = 0    
        wait_time    = 0    
        ride_time    = 0  
        
        # Derive the current location, time, day and request locations        
        curr_loc,curr_time,curr_day=self.getstate_currstate_currloc_time_day(state)
        pickup_loc,drop_loc=self.getaction_pickup_drop_loc(action)
          
        if ((pickup_loc== 0) and (drop_loc == 0)):
            # No ride picked
            wait_time = 1
            next_loc = curr_loc
        elif (curr_loc == pickup_loc):
            # driver in pickup location alredy
            ride_time = Time_matrix[curr_loc][drop_loc][curr_time][curr_day]            
            # next location is the drop location
            next_loc = drop_loc
        else:
            # Driver to pickup loc
            transit_time      = Time_matrix[curr_loc][pickup_loc][curr_time][curr_day]
            new_time, new_day = self.get_new_time_day(curr_time, curr_day, transit_time)
            
            # pickup to drop loc
            ride_time = Time_matrix[pickup_loc][drop_loc][new_time][new_day]
            next_loc  = drop_loc

        # Calculate total time as sum of all durations
        total_time = (wait_time + transit_time + ride_time)
        next_time, next_day = self.get_new_time_day(curr_time, curr_day, total_time)
        next_state = [next_loc, next_time, next_day]


        return next_state, wait_time, transit_time, ride_time
    
    def step(self, state, action, Time_matrix):
        """
        Take a trip as cabby to get rewards next step and total time spent
        """
        # Get the next state and the various time durations
        next_state, wait_time, transit_time, ride_time = self.next_state_func(
            state, action, Time_matrix)

        # Calculate the reward based on the different time durations
        rewards = self.reward_func(wait_time, transit_time, ride_time)
        total_time = wait_time + transit_time + ride_time
        
        return next_state,rewards, total_time

    def reset(self):
        return self.action_space, self.state_space, self.state_init

    def getstate_currstate_currloc_time_day(self,state):
        return state[0],state[1],state[2]
    
    def getaction_pickup_drop_loc(self,action):
        return action[0],action[1]

    def get_new_time_day(self, time, day, ride_time):
        """
        Takes in the current state and time taken for driver's journey to return
        the state post that journey.
        """
        ride_time = int(ride_time)

        if (time + ride_time) < 24:
            time = time + ride_time
        else:
            time = (time + ride_time) % 24             
            num_days = (time + ride_time) // 24
            day = (day + num_days ) % 7

        return time, day

