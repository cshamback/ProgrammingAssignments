import time
import math
from functools import cache

money = [100,101,102,1012]
def RecursiveDP(earnings, time, memo={}):
    # want to keep memo to store previous values and things
    if memo is None:
        memo = {}
    # checks when to stop
    if time == len(earnings):
        return 0, memo
    
    #goes through the entire list of money earned
    for x in earnings:
        # if value is already in the memo then return it
        if(tuple(earnings) in memo):
            return memo[time], memo
        else:
            # otherwise, add it to the memo and find out sometime later
            currentEarnings = earnings[time] + RecursiveDP(earnings,time + 1,memo)[0]
            memo[f"Task {time}"] = currentEarnings
            return currentEarnings, memo



   
    # Have all the user's times stored in the array
    # Create a memo and have program check if already in there
    # If not, then just add it to the memo
    # Recursively do this until end of array
    # Sort the times using merge sort (thank you cody)
    # Add all earnings and print into the skeleton


# test runs
total, answer = RecursiveDP(money, 1)
print(total)
print("--------")
print(answer)
