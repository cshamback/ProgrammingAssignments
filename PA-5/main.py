# UI/MAIN 
from task import *
from merge import *
import time
from bf import brute_force_maximize_earnings
from custom_algorithm import find_max_sets 
from dp import *
from RevisionRecursionReintegrate import *

while True:
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

# Measures Execution Time and Run Algorithms for brute force
    start_time = time.time()
    best_schedules, max_earning = brute_force_maximize_earnings(tasks)
    elapsed_time = (time.time() - start_time) * 1000 #converts to ms

# Print Results of Time and Earnings for Brute Force Algorithm
    print() #spacing
    print(f"The time elapsed in the brute-force algorithm is {elapsed_time:.6f} ms and value is {max_earning}")

# Measures Execution time for Recursive Dynamic Programming Algorithm
    start_time = time.time()
    maxprofit, rdp_max_profit = RecursiveDP(tasks)
    elapsed_time = (time.time() - start_time) * 1000 #converts to ms

# Print Results of Time and Earnings for Recursive Dynamic Programming Algorithm
    print(f"The time elapsed in the recursive dynamic programming algorithm is {elapsed_time:.6f} ms and value is {rdp_max_profit}")

# Measures Execution time for Dynamic Programming Algorithm
    start_time = time.time()
    maxProfit = dp(tasks)
    elapsed_time = (time.time() - start_time) * 1000 #converts to ms

    # Print Results of Time and Earnings for Dynamic Programming Algorithm
    print(f"The time elapsed in the non-recursive dynamic programming algorithm is {elapsed_time:.6f} ms and value is {maxProfit}")

    # Print Best Schedule for Max Earnings
    print("\nThe best schedule for maximum earnings is: ")
    for idx, schedule in enumerate(best_schedules, 1):
        task_order = " -> ".join(task.name for task in schedule)
        total_earning = sum(task.pay for task in schedule)
        print(f"Option {idx}: {task_order}, with a total earning of {maxProfit}")

    # Calls find max sets function from custom_algorithm.py
    start_time = time.time()
    find_max_result = find_max_sets(tasks) #changed variable name so it doesn't overwrite itself if user continues

    # Identify the best schedule(s) and remove them from "other options"
    best_schedule = best_schedules[0] if best_schedules else None
    other_options = [schedule for schedule in find_max_result if schedule != best_schedule]
    num_other_options = len(other_options)  # Correct count after filtering

    # Prints all options
    print(f"\nHere are different options of sets of tasks to select from.")
    
    for idx, schedule in enumerate(other_options, 1):  # Print only "other" schedules
        task_order = " -> ".join(task.name for task in schedule)
        total_earning = sum(task.pay for task in schedule)
        print(f"Option {idx}: {task_order}, with a total earning of {total_earning}")

    # Continuation Prompt
    while True:
        cont = input("\nWould you like to continue and enter new tasks? (y/n): \n").strip().lower()
    
        if cont == "y":
            print("\nRestarting the program...\n")
            break  # breaks out inner loop and restarts main loop

        elif cont == "n":
            print("\nGoodbye!\n")
            exit() #exits the program entirely

        else:
            print("Invalid input. Please enter 'y' or 'n'.")
