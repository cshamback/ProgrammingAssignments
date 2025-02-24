from Testing_PlayGround import *
from csvGen import *
import time

recordToSpreadsheet = []
while True:
    try:
        answer = int(input("Select 1 for Dynamic Programming Fibonacci and select 2 for Recursive Fibonacci. Or press anything else to quit. "))
        if(answer == 1):
            # limit = n, which is largest fibonacci value to compute 
            Limit = int(input("Give me the input of n. "))
            x = dynamicFib(Limit)
            recordToSpreadsheet.append(statistics(Limit,x,recursiveCalculations(Limit), dynamicCalculations(Limit),scaledItems(Limit),aggregateTime(Limit)))
            generateCsv("Test1", recordToSpreadsheet)
        elif(answer == 2):
            Limit = int(input("Give me the input of n. "))
            for i in range(Limit+1): # up to AND including limit
                print(recursiveFib(i))
            print("Recursion Complete") 
        else:
            print("Pick 1 or 2.")   
    except ValueError:
        break