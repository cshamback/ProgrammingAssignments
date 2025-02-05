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
for instance in range (10):
    #Create a sub array so that we can append to the big array to get our 9 different arrays.
    subArray = []

    #Fills the array with up to 20 elements. It can be any number, I just did 20 so my computer won't die.
    for i in range(instance * 1):
        #The values of said elements are between 1 and 99
        subArray.append(randomNumberFill(1,99))
    bigArray.append(subArray) 
# ------------------------------------------------------------------------
# SORT SECTION =============================================================
# ------------------------------------------------------------------------
# Iterates through every element in the bigArray array
for list in bigArray:
    #starts recording the time
    start = time.time()
    # Sorting the current element using merge sort
    mergeSort(0,len(list),list)
    # Stops recording the time and subtracts from the start to get the elapsed time
    end = time.time()
    elapsed = end - start
    # prints out the elapsed time
    print("%.10f" % elapsed)
# ------------------------------------------------------------------------
# UI SECTION =============================================================
# ------------------------------------------------------------------------

# Step 1 - tell user they can input a number 1 ... 9 and press any other key to escape   

#this while operation allows multiple instances of this without needing to restart the program
while True:
    try:
        # User selects an array to see
        SelectedArray = int(input("Select a number from 1 to 9 inclusive. Or you can type 'EXIT' to leave. "))
    
        if(SelectedArray > 0 and SelectedArray <= 9): # x can be 0-8, for indexes in bigArray
            print(f"There are {len(bigArray[SelectedArray])} elements in Array_{SelectedArray}")
 
            #Displays the array before it was sorted
            print(f"Displaying Array_{SelectedArray}")
            print(bigArray[SelectedArray])

            #Displays the array after it was sorted
            print(f"Displaying sorted Array_{SelectedArray}")
            print(mergeSort(0,len(bigArray[SelectedArray])),bigArray[SelectedArray])
        else:
            # Just in case the user's input is out of the range
            print("Try again")     
    except ValueError:
        # In case the user types anything that isn't an integer 
        print("Exiting...")
        break

# Components of loop
#   Step 1 - Create an array [Done]
#   Step 2 - Fill array with random numbers [Done]
#   Step 3 - Put in csv [NOT Done]
#   Step 4 - Repeat 8 more times [Done?]
