# UI/MAIN 
from task import *
from merge import *
import time
from bf import brute_force_maximize_earnings

numTasks = int(input("Enter the number of all paid tasks: "))
i = 0

# task objects are defined in task.py
# each has a start, end, and pay attribute with getters for each. 
# no setters are needed since these values are never changed after construction. 

tasks = []

# get all tasks
while(i < numTasks):
    print()
    currEarning = int(input("Enter the amount earned by task " + str(i + 1) + ": "))
    currStart = int(input("Enter the start time of the task: "))
    currEnd = int(input("Enter the end time of the task: "))

    currTask = Task(currEarning, currStart, currEnd, "Task " + str(i + 1))
    tasks.append(currTask)

    i = i + 1

print()

# sort tasks by end time in asc. order (starting from 0)
sortedTasks = mergeSort(0, len(tasks), tasks)
tasks = sortedTasks

print("+--------------------------------------------------+")
print("| Task Number | Start Times | End Times | Earnings |")
print("+--------------------------------------------------+") 

for i in range(numTasks):
    numSpaces1 = len("| Task Number ") - len(str(tasks[i].name))
    numSpaces2 = len("| Start Times ") - len(str(tasks[i].start))
    numSpaces3 = len("| End Times ") - len(str(tasks[i].end))
    numSpaces4 = len("| Earnings ") - len(str(tasks[i].pay)) - 2

    print("| " + str(tasks[i].name) + (" " * numSpaces1) + str(tasks[i].start) + (" " * numSpaces2) + str(tasks[i].end) + (" " * numSpaces3) + str(tasks[i].pay) + (" " * numSpaces4) + "|")

print("+--------------------------------------------------+") 

# Measures Execution Time and Run Algorithms
start_time = time.time()
best_schedules, max_earning = brute_force_maximize_earnings(tasks)
elapsed_time = (time.time() - start_time) * 1000 #converts to ms

# Print Results of Time and Earnings
print(f"The time elapsed in the brute-force algorithm is {elapsed_time:.6f} ms and value is {max_earning}")

# Print Best Schedule for Each Approach
print("Best schedule for brute force method: ")
for idx, schedule in enumerate(best_schedules, 1):
    task_order = " -> ".join(task.name for task in schedule)
    print("Option {}: {}, with a total earning of {}".format(idx, task_order, max_earning))

# Continuation Prompt
while True:
    cont = input("Would you like to continue? (y/n): ").strip().lower()
    if cont == "y":
        break
    elif cont == "n":
        print("Goodbye!")
        break
    else:
        print("Invalid input. Please enter 'y' or 'n'.")
        continue
