from Fibonacci import recursiveCalculations, recursiveFib, dynamicCalculations, dynamicFib, aggregateTime, scaledItems
from csvGen import generateCsv, statistics
import time

recordToSpreadsheet = []
# Creates and fills out the following spreadsheet information onto a different file
# We decided to do this first since it might take a while.
AllocationList = [10,12,15,20,23,25,30]
for i in AllocationList:

    # Does both dynamic and recursive methods first and gets the timings for both.
    t1 = recursiveCalculations(i)
    t2 = dynamicCalculations(i)
    agTime = aggregateTime(t1, t2) # or agTime = t1 / t2
    # Saves it in the array and then writes it to the spreadsheet in the next line
    recordToSpreadsheet.append(statistics(i,dynamicFib(i),t1, t2,scaledItems(i),agTime))
generateCsv("Fibonacci_Time", recordToSpreadsheet)


# This allows the program to keep asking the user for an input
# of which method of fibonacci they want and F(n) they want to see.
# It keeps doing this until the user presses or types something it doesn't agree with
# ,being 1 or 2, and ends the program. 
while True:
    # Ensures guaranteed execution in case anything goes wrong
    try:
        answer = int(input("Select 1 for Dynamic Programming Fibonacci and select 2 for Recursive Fibonacci. Or press anything else to quit. "))
        # 1 for dynamic fibonacci
        if(answer == 1):
            # limit = n, which is largest fibonacci value to compute 
            Limit = int(input("Give me the input of n. "))
            print(dynamicFib(Limit))
        # 2 for recursive fibonacci
        elif(answer == 2):
            Limit = int(input("Give me the input of n. "))
            print(recursiveFib(Limit))

        # In the event the user inputs anything other than 1 or 2
        else:
            print("Pick 1 or 2.") 
        # In the event the user wants to exit, so they type anything else  
    except ValueError:
        break