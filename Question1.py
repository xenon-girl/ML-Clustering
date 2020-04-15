##Problem Statement 1 : Say you are standing at the bottom of a staircase with
##a dice. With each throw of the dice you either move down one step
##(if you get a 1 or 2 on the dice) or move up one step
##(if you get a 3, 4 or 5 on the dice).
##If you throw a 6 on the dice, you throw the dice again
##and move up the staircase by the number you get on that second throw.
##Note if you are on the base of the staircase you cannot move down!
##What is the probability that you will reach more than 60 steps after
##250 throws of the dice. Change the code so that you have a function that
##takes as parameter, the number of throws Add a new parameter to the
##function that takes a probability distribution over all
##outcomes from a dice throw. For example (0.2,0.3,0.2,0.1,0.1,0.1)
##would suggest that the probability of getting a 1 is 0.2, 2 is 0.3 etc.
##How does that change the probability of reaching a step higher than 60?


import numpy as np

def step_prob(threshold_step, number_of_throws, prob_dist):
    per = 0
    for i in range(1000):
        step = 0
        for _ in range(number_of_throws):
            dice = np.random.choice(np.arange(1, 7), p=prob_dist)
            if dice<3:
                step = max(0, step-1)
            elif dice<6:
                step = step+1
            else:
                dice = np.random.choice(np.arange(1, 7), p=prob_dist)
                step += dice
        
        if step>threshold_step:
            per += 1
            
    return per/10
        
                
print(step_prob(60, 250,[0.2,0.3,0.2,0.1,0.1,0.1]))
