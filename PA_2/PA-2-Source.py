from csvGen import * 
from mergeSort import * 

import time

# ------------------------------------------------------------------------
# PREMADE ARRAYS =========================================================
# ------------------------------------------------------------------------

# fill out 9 arrays
#This big array would hold all our arrays and make interacting with the user much easier.
bigArray = []

#Because arrays start at index 0, we have to make it repeat this 8 times to get our 9 arrays.
for instance in range (1,10):
    #Create a sub array so that we can append to the big array to get our 9 different arrays.
    subArray = [randomNumberFill(1,99) for _ in range(instance * 1000)]
    bigArray.append(subArray)

    #Fills the array with up to 20 elements. It can be any number, I just did 20 so my computer won't die.
    for i in range(instance * 1000):
        #The values of said elements are between 1 and 99
        subArray.append(randomNumberFill(1,99))
    bigArray.append(subArray) 

# ------------------------------------------------------------------------
# SPREADSHEET SECTION ====================================================
# ------------------------------------------------------------------------

spreadsheetList = [] # one row per array, all start empty

# merge sort all 9 arrays
for i, sublist in enumerate(bigArray): 
    # merge sort each array and get the time elapsed 
    startTime = time.time()
    mergeSort(0, len(sublist) - 1, sublist)
    endTime = time.time()

    elapsedTime = endTime - startTime

    #print(f"startTime: {startTime}, endTime: {endTime}, elapsedTime: {elapsedTime}")

    # generate the current row in the spreadsheet 
    spreadsheetList.append(getStats(sublist, elapsedTime))

# export spreadsheet as .csv file
csvGen("Mergesort_Time", spreadsheetList)

# ------------------------------------------------------------------------
# UI SECTION =============================================================
# ------------------------------------------------------------------------

# Step 1 - tell user they can input a number 1 ... 9 and press any other key to escape   

#this while operation allows multiple instances of this without needing to restart the program
while True:
    try:
        x = int(input("Select a number from 1 to 9 inclusive. Or you can type 'EXIT' to leave. "))
        x = x - 1 # allow for 0 indexing while also letting user pick 1...9
    
        if(x >= 0 and x < 9): # x can be 0-8, for indexes in bigArray
            print(f"There are {len(bigArray[x])} elements in Array_{x + 1}")
 
            #Displays the array before it was sorted
            print(f"Displaying Array_{x + 1}")
            print(bigArray[x])

            #Displays the array after it was sorted
            sorted_array = mergeSort(0, len(bigArray[x]) - 1, bigArray[x][:])
            print(f"Displaying sorted Array_{x + 1}")
            print(sorted_array)
        else:
            print("Try again")     
    except ValueError:
        print("Exiting...")
        break

# Components of loop
#   Step 1 - Create an array [Done]
#   Step 2 - Fill array with random numbers [Done]
#   Step 3 - Put in csv [NOT Done]
#   Step 4 - Repeat 8 more times [Done?]
