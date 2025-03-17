# UI/MAIN 

numTasks = int(input("Enter the number of all paid tasks: "))
i = 0

# duration and earnings for each task are stored in these arrays
# index corresponds to task number 
# ie. task #3 is the 3rd one the user inputs values for, and it's in index 2 of both arrays.
earnings = []
starts = []
ends = []

while(i < numTasks):
    currEarning = int(input("Enter the amount earned by task " + str(i + 1) + ": "))
    currStart = int(input("Enter the start time of the task: "))
    currEnd = int(input("Enter the end time of the task: "))

    earnings.append(currEarning)
    starts.append(currStart)
    ends.append(currEnd)

    i = i + 1

print("+--------------------------------------------------+")
print("| Task Number | Start Times | End Times | Earnings |")
print("+--------------------------------------------------+") 

for i in range(numTasks):
    numSpaces1 = len("| Task Number ") - len(str(i))
    numSpaces2 = len("| Start Times ") - len(str(starts[i]))
    numSpaces3 = len("| End Times ") - len(str(ends[i]))
    numSpaces4 = len("| Earnings ") - len(str(earnings[i])) - 2

    print("| " + str(i) + (" " * numSpaces1) + str(starts[i]) + (" " * numSpaces2) + str(ends[i]) + (" " * numSpaces3) + str(earnings[i]) + (" " * numSpaces4) + "|")

print("+--------------------------------------------------+") 