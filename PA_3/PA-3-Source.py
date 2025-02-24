from Testing_PlayGround import *
from csvGen import *
import time

recordToSpreadsheet = []
AllocationList = [10,12,15,20,23,25,30]
for i in AllocationList:
    recordToSpreadsheet.append(statistics(i,dynamicFib(i),recursiveCalculations(i), dynamicCalculations(i),scaledItems(i),aggregateTime(i)))

generateCsv("Test1", recordToSpreadsheet)

while True:
    try:
        answer = int(input("Select 1 for Dynamic Programming Fibonacci and select 2 for Recursive Fibonacci. Or press anything else to quit. "))
        if(answer == 1):
            # limit = n, which is largest fibonacci value to compute 
            Limit = int(input("Give me the input of n. "))
            print(dynamicFib(Limit))
        elif(answer == 2):
            Limit = int(input("Give me the input of n. "))
            print(recursiveFib(Limit))
            
        else:
            print("Pick 1 or 2.")   
    except ValueError:
        break