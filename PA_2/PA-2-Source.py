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

#this while operation allows multiple instances of this without needing to restart the program
while True:
    try:
        x = int(input("Select a number from 1 to 9 inclusive. "))
        if(x > 0 and x < 10):
            print(f"There are {len(bigArray[x])} elements in Array_{x}")
            #Displays the array before it was sorted
            print(f"Displaying Array_ {x}")
            print(bigArray[x])
            #Displays the array after it was sorted
            print(f"Displaying sorted Array_{x}")
            print(mergeSort(0,len(bigArray[x]),bigArray[x]))
            break
        else:
            print("Try again")     
    except ValueError:
        print("Try again")
        break

# Components of loop
#   Step 1 - Create an array [Done]
#   Step 2 - Fill array with random numbers [Done]
#   Step 3 - Put in csv [NOT Done]
#   Step 4 - Repeat 8 more times [Done?]
