#from gym import spaces
import numpy as np
import random
from itertools import groupby
from itertools import product


class TicTacToe():

    def __init__(self):
        """initialise the board"""
        
        # initialise state as an array
        self.state = [np.nan for _ in range(9)]  # initialises the board position, can initialise to an array or matrix
        # all possible numbers
        self.all_possible_numbers = [i for i in range(1, len(self.state) + 1)] # , can initialise to an array or matrix

        self.reset()


    def is_winning(self, curr_state):
        """Takes state as an input and returns whether any row, column or diagonal has winning sum
        Example: Input state- [1, 2, 3, 4, nan, nan, nan, nan, nan]
        Output = False"""
        
        #helper function to calculate total given a set of indexes; returns True if total is 15.
        def is_total_15(idx_set):
            for idx_list in idx_set:
                sum=0
                for idx in idx_list:
                    sum += curr_state[idx]
                if (sum==15):
                    return True
            return False
        
        #indexes for totalling rows
        idx_set = [[0,1,2],[3,4,5],[6,7,8]]
        if (is_total_15(idx_set)):
            return True
        
        #indexes for totalling columns
        idx_set = [[0,3,6],[1,4,7],[2,5,8]]
        if (is_total_15(idx_set)):
            return True
                
        #indexes for totalling diagonals
        idx_set = [[0,4,8],[2,4,6]]
        if (is_total_15(idx_set)):
            return True
            
        return False
    
    
    def is_terminal(self, curr_state):
        # Terminal state could be winning state or when the board is filled up

        if self.is_winning(curr_state) == True:
            return True, 'Win'
        elif len(self.allowed_positions(curr_state)) == 0:
            return True, 'Tie'
        else:
            return False, 'Resume'


    def allowed_positions(self, curr_state):
        """Takes state as an input and returns all indexes that are blank"""
        return [i for i, val in enumerate(curr_state) if np.isnan(val)]


    def allowed_values(self, curr_state):
        """Takes the current state as input and returns all possible (unused) values that can be placed on the board"""

        used_values = [val for val in curr_state if not np.isnan(val)]
        agent_values = [val for val in self.all_possible_numbers if val not in used_values and val % 2 !=0]
        env_values = [val for val in self.all_possible_numbers if val not in used_values and val % 2 ==0]

        return (agent_values, env_values)


    def action_space(self, curr_state):
        """Takes the current state as input and returns all possible actions, i.e, all combinations of allowed positions 
        and allowed values"""

        agent_actions = product(self.allowed_positions(curr_state), self.allowed_values(curr_state)[0])
        env_actions = product(self.allowed_positions(curr_state), self.allowed_values(curr_state)[1])
        return (agent_actions, env_actions)


    def state_transition(self, curr_state, curr_action):
        """Takes current state and action and returns the board position just after agent's move.
        Example: Input state- [1, 2, 3, 4, nan, nan, nan, nan, nan], action- [7, 9] or [position, value]
        Output = [1, 2, 3, 4, nan, nan, nan, 9, nan]
        """
        new_state = [elem for elem in curr_state]
        new_state[curr_action[0]]=curr_action[1]
        return new_state


#    def step(self, curr_state, curr_action):
    def step(self, curr_state, curr_action, prt_offset=''):
        """Takes current state and action and returns the next state, reward and whether the state is terminal. 
        
        Hint: First, check the board position after agent's move, whether the game is won/loss/tied. Then incorporate
        environment's move and again check the board status.
        
        Example: Input state- [1, 2, 3, 4, nan, nan, nan, nan, nan], action- [7, 9] or [position, value]
        Output = ([1, 2, 3, 4, nan, nan, nan, 9, nan], -1, False)"""
        
        def dprint(*argv):
            for arg in argv:
                print(prt_offset,arg)
        
        #
        #make the agent move which is chosen above and gather the state for the agent move
        agt_state = self.state_transition(curr_state, curr_action)
        #check board position after agent's move as passed in via curr_state
        term_state_flg, outcome = self.is_terminal(agt_state)
        
        #set next state as state after agent's move, which will be the case if outcome is Win or Tie.
        nxt_state = agt_state  
        
#        dprint('Outcome after agent move:', outcome)
        #check outcome of agent's move based on is_terminal above
        if (outcome == 'Win'):
        # if current state shows a Win, the agent has Won and hence reward is +10
            reward = +10
        elif (outcome == 'Tie'):
        # if current state shows a Tie, board is full, hence terminal state an reward is 0
            reward = 0 
        elif (outcome == 'Resume'):
        # if current state is neither Win nor Tie, that means, game resumes and it is now the environment's turn to play
            #play the environment's move
            
            #play the environment's move
#            dprint('Evaluating Environment"s move')
            agt_actions, env_actions = self.action_space(agt_state)
#            dprint('Action space for Env:')

            env_actions_list = [item for item in env_actions]
#            print(env_actions)
            agt_moves, env_moves = self.allowed_values(agt_state)
#            dprint('Allowed values for Env:',env_moves )
#            dprint('Allowed positions:', self.allowed_positions(agt_state))
            
            env_action = env_actions_list[np.random.choice(np.arange(len(env_actions_list)))]
#            dprint('Env Action:', env_action)
                
            nxt_state = self.state_transition(agt_state,env_action)
#            dprint('State after env action:', nxt_state)

            # check the outcome of environment's move above
            term_state_flg, outcome = self.is_terminal(nxt_state)
            
#            dprint('Outcome after env move:', outcome)

            if (outcome == 'Win'):
            # if state after env move shows a Win, the env has Won and hence and reward is -10
                reward = -10
            elif (outcome == 'Tie'):
            # if state after env move shows a Tie, board is full, hence terminal state and reward is 0
                reward = 0
            elif (outcome == 'Resume'):
            # if state after env move shows neither a Win nor a tie, game continues, hence reward is -1 and terminal is False
                reward = -1

        return nxt_state, reward, term_state_flg

    def reset(self):
        return self.state
