# UI/MAIN 

numTasks = int(input("Enter the number of all paid tasks: "))
i = 0

# duration and earnings for each task are stored in these arrays
# index corresponds to task number 
# ie. task #3 is the 3rd one the user inputs values for, and it's in index 2 of both arrays.
earnings = []
durations = []

while(i < numTasks):
    currEarning = int(input("Enter the amount earned by task " + str(i + 1) + ": "))
    currTime = int(input("Enter the duration of the task: "))

    earnings.append(currEarning)
    durations.append(currTime)
    
    i = i + 1

for i in range(numTasks):
    print("Task " + str(i) + " duration: " + str(durations[i]) + " earnings: " + str(earnings[i]))