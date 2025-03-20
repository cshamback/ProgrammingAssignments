# UI/MAIN 
from task import *
from merge import *
import time
from bf import brute_force_maximize_earnings
from custom_algorithm import find_max_sets 
from dp import *

# numTasks = int(input("Enter the number of all paid tasks: "))
numTasks = 4
i = 0

# task objects are defined in task.py
# each has a start, end, and pay attribute with getters for each. 
# no setters are needed since these values are never changed after construction. 

tasks = []

# get all tasks
"""
while(i < numTasks):
    print()
    currEarning = int(input("Enter the amount earned by task " + str(i + 1) + ": "))
    currStart = int(input("Enter the start time of the task: "))
    currEnd = int(input("Enter the end time of the task: "))

    currTask = Task(currEarning, currStart, currEnd, "Task " + str(i + 1))
    tasks.append(currTask)

    i = i + 1
"""
tasks = [Task(10, 0, 1, "Task 1"), Task(11, 1, 2, "Task 2"), Task(9, 5, 6, "Task 3"), Task(14, 5, 9, "Task 4")]

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

start_time = time.time()
dp(tasks)
elapsed_time_DP = (time.time() - start_time) * 1000 #converts to ms

# Print Results of Time and Earnings
print() #spacing
print(f"The time elapsed in the brute-force algorithm is {elapsed_time:.6f} ms and value is {max_earning}")
print(f"The time elapsed in the non-recursive DP algorithm is {elapsed_time_DP:.6f} ms and value is {max_earning}")

# Print Best Schedule for Each Approach
print("Best schedule for each algorithm: ")
for idx, schedule in enumerate(best_schedules, 1):
    task_order = " -> ".join(task.name for task in schedule)
    print("{}, with a total earning of {}".format(task_order, max_earning))

# Calls find max sets function from custom_algorithm.py
start_time = time.time()
find_max_sets = find_max_sets(tasks)

# Print Results of Custom Algorithm
print(f"\nThere are {len(find_max_sets)} options to select different sets of tasks.")
for idx, schedule in enumerate(find_max_sets, 1):
    task_order = " -> ".join(task.name for task in schedule)
    total_earning = sum(task.pay for task in schedule) 
    print(f"Option {idx}: {task_order}, with a total earning of {total_earning}".format(idx, task_order, total_earning))

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
