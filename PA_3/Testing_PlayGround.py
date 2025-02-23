# This file is to just test out code or ideas. When done, please revert it back to how it was.
# I mean, delete everything below the designated row.

#---------------------------------------------------------------------
#Start Below =========================================================
#---------------------------------------------------------------------
# note: both algorithms start at n = 0. 
# that is, fib(0) = 1 and fib(1) = 1. 
import time
import math
def recursiveFib(n):
    # base case: fib(0) is 1 and fib(1) is 1
    if(n <= 1):
        return 1
        
    # otherwise, fib(n) is the sum of the two previous values 
    return recursiveFib(n - 1) + recursiveFib(n - 2)
    
def dynamicFib(n):
    # base case: fib(0) and fib(1) are both 1
    if(n <= 1):
        return 1
        
    # dict stores all fib(n) found so far 
    # key = n, value = fib(n)
    memo = {}
    
    # start at n = 2 and find all solutions up to n
    currentFib = 0
    for i in range(2, n + 1):
        # check if dict already contains the solution
        # that is, if it already has a value for the key n 
        if(n in memo):
            # get solution from dict
            return memo[n]
        else:
            # calculate solution and store in dict 
            currentFib = dynamicFib(n - 1) + dynamicFib(n - 2)
            memo[n] = currentFib
            
            return currentFib; 
            
    return memo[n] # get nth fibonacci number from dict 

def dynamicCalculations(Limit):
    startTimeD = time.time()
    x = dynamicFib(Limit-1)
    endTimeD = time.time()
    elapsedTimeD = endTimeD - startTimeD
    return elapsedTimeD

def recursiveCalculations(Limit):
    startTimeR = time.time()
    x = recursiveFib(Limit-1)
    endTimeR = time.time()
    elapsedTimeR = endTimeR - startTimeR
    return elapsedTimeR

def aggregateTime(Limit):
    result = float(recursiveCalculations(Limit)/dynamicCalculations(Limit))
    return result 

def scaledItems(n):
    Result = (math.pow(2,n)) / n
    return Result