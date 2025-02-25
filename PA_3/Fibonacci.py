import time
import math

def recursiveFib(n):
    # base case: fib(0) is 0, fib(1) and fib(2) 1
    if(n == 0):
        return 0
    if(n <= 2):
        return 1
        
    # otherwise, fib(n) is the sum of the two previous values 
    return recursiveFib(n - 1) + recursiveFib(n - 2)
    
def dynamicFib(n):
    # base case: fib(0) is 0, fib(1) and fib(2) are 1
    if(n == 0):
        return 0
    if(n <= 2):
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

# get amount of time it takes to do dynamic fibonacci 
def dynamicCalculations(Limit):
    startTimeD = time.time()
    x = dynamicFib(Limit)
    endTimeD = time.time()
    elapsedTimeD = endTimeD - startTimeD
    return elapsedTimeD

# get amount of time it takes to do recursive fibonacci 
def recursiveCalculations(Limit):
    startTimeR = time.time()
    x = recursiveFib(Limit)
    endTimeR = time.time()
    elapsedTimeR = endTimeR - startTimeR
    return elapsedTimeR

# get recursive time / dynamic time -> "how much faster is dynamic than recursive alg"
# ie. if recursive = 3 and dynamic = 1, 3/1 = 3 so dynamic is 3x faster

def aggregateTime(L1, R2):
    # temporary solution: if we are going to divide by 0, don't
    # assume that if one dynamic calculation time is 0 it's because n is very low, so both are 0. 
    try:
        result = float(recursiveCalculations(L1)/dynamicCalculations(R2))

        print(recursiveCalculations(L1), " / ", dynamicCalculations(R2), " = ", result)
        print()
    except ZeroDivisionError:
        result = float('0.0')
    return result
        

def scaledItems(n):
    Result = float((math.pow(2,n)) / n)
    return Result