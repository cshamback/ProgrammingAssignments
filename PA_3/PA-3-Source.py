from Testing_PlayGround import *
from csvGen import *
import time

recordToSpreadsheet = []
while True:
    try:
        answer = int(input("Select 1 for Dynamic Programming Fibonacci and select 2 for Recursive Fibonacci. Or press anything else to quit. "))
        if(answer == 1):
            Limit = int(input("Give me the input of n. "))
            x = dynamicFib(Limit-1)
            recordToSpreadsheet.append(statistics(Limit,x,recursiveCalculations(Limit-1), dynamicCalculations(Limit-1),scaledItems(Limit-1),aggregateTime(Limit-1)))
            generateCsv("Test1", recordToSpreadsheet)
        elif(answer == 2):
            Limit = int(input("Give me the input of n. "))
            for i in range(Limit):
                print(recursiveFib(i))
            print("Recursion Complete") 
        else:
            print("Pick 1 or 2.")   
    except ValueError:
        break