from csvGen import * 
from mergeSort import * 


# ------------------------------------------------------------------------
# PREMADE ARRAYS =========================================================
# ------------------------------------------------------------------------

# fill out 9 arrays (might want to )
# 
# merge sort each row, get data (2D array, used for csv input)

# ------------------------------------------------------------------------
# UI SECTION =====================================================================
# ------------------------------------------------------------------------

# Step 1 - tell user they can input a number 1 ... 9 and press any other key to escape 
# Stage 1 - A very basic input prompt to serve as a skeleton. Likely overcomplicated it...
#This big array would hold all our arrays and make interacting with the user much easier.
bigArray = []
#Because arrays start at index 0, we have to make it repeat this 8 times to get our 9 arrays.
for instance in range (8):
    #Create a sub array so that we can append to the big array to get our 9 different arrays.
    subArray = []
    #Fills the array with up to 20 elements. It can be any number, I just did 20 so my computer won't die.
    for i in range(randomNumberFill(1,20)):
        #The values of said elements are between 1 and 99
        subArray.append(randomNumberFill(1,99))
    bigArray.append(subArray)   

userInput = input("Input a number between 0 and 8 [inclusive]. Enter any other value or key to escape. ")
if userInput.isnumeric() == True:
    #Had to force the user's input to become a string. It would've stayed as a char otherwise.
    x = int(userInput)
    #Checks if the inputted number is between 1 and 9
    if x >= 1 and x <= 9:
        print(f"There are {len(bigArray[x])} elements in Array_{x}")
        #Displays the array before it was sorted
        print(f"Displaying Array_ {x}")
        print(bigArray[x])
        #Displays the array after it was sorted
        print(f"Displaying sorted Array_{x}")
        print(mergeSort(0,len(bigArray[x]),bigArray[x]))
    #This is for the edge case that user types in a number that isn't between 1 and 9
    else:
        print("Invalid key pressed. Escaping...")
#This is for when the user doesn't type in a number at all
else:
    print("Invalid key pressed. Escaping...")
# Components of loop
#   Step 1 - Create an array
#   Step 2 - Fill array with random numbers
#   Step 3 - Put in csv
#   Step 4 - Repeat 8 more times
# Step 3 - Have the user enter a number from 1 - 9 inclusive (I guess done). At the same time, sort the inputted index.
# Step 4 - display Array_i 
# Step 5 - display Sorted_Array_i