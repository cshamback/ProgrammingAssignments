from task import *
from merge import *

# RECREATION OF EVERYTHING FOR TESTING STUFF
numTasks = int(input("Enter the number of all paid tasks: "))

tasks = []
for i in range(numTasks):
    print()
    currEarning = int(input(f"Enter the amount earned by task {i + 1}: "))
    currStart = int(input("Enter the start time of the task: "))
    currEnd = int(input("Enter the end time of the task: "))

    tasks.append(Task(currEarning, currStart, currEnd, f"Task {i + 1}"))


def RecursiveDP(taskQueue):
    memo = {}  # Initialize a fresh dictionary

    for i, task in enumerate(taskQueue):  # Ensure we iterate properly
        memo[i] = task

    return memo

formatted_memo = RecursiveDP(tasks)
for key, value in formatted_memo.items():
    print(f"{{{key}: {value}}}")

    
