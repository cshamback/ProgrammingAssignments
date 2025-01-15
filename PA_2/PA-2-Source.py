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
"""userInput = input("Input a number between 1 and 9 [inclusive]. Enter any other value or key to escape. ")
if userInput.isnumeric() == True:
    print("PASS")
    x = int(userInput)
    if x >= 1 and x <= 9:
        print("PASS")

else:
    print("Bye!")

"""
# Components of loop
#   Step 1 - Create an array
#   Step 2 - Fill array with random numbers
#   Step 3 - Put in csv
#   Step 4 - Repeat 8 more times
# Step 3 - Have the user enter a number from 1 - 9 inclusive (I guess done). At the same time, sort the inputted index.
# Step 4 - display Array_i 
# Step 5 - display Sorted_Array_i