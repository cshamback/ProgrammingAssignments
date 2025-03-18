# UI/MAIN 
from task import *
from merge import *

numTasks = int(input("Enter the number of all paid tasks: "))
i = 0

# task objects are defined in task.py
# each has a start, end, and pay attribute with getters for each. 
# no setters are needed since these values are never changed after construction. 

tasks = []

# get all tasks
while(i < numTasks):
    currEarning = int(input("Enter the amount earned by task " + str(i + 1) + ": "))
    currStart = int(input("Enter the start time of the task: "))
    currEnd = int(input("Enter the end time of the task: "))

    currTask = Task(currEarning, currStart, currEnd)
    tasks.append(currTask)

    i = i + 1

# sort tasks by end time in asc. order (starting from 0)
sortedTasks = mergeSort(0, len(tasks), tasks)
tasks = sortedTasks;

print("+--------------------------------------------------+")
print("| Task Number | Start Times | End Times | Earnings |")
print("+--------------------------------------------------+") 

for i in range(numTasks):
    numSpaces1 = len("| Task Number ") - len(str(i + 1))
    numSpaces2 = len("| Start Times ") - len(str(tasks[i].start))
    numSpaces3 = len("| End Times ") - len(str(tasks[i].end))
    numSpaces4 = len("| Earnings ") - len(str(tasks[i].pay)) - 2

    print("| " + str(i + 1) + (" " * numSpaces1) + str(tasks[i].start) + (" " * numSpaces2) + str(tasks[i].end) + (" " * numSpaces3) + str(tasks[i].pay) + (" " * numSpaces4) + "|")

print("+--------------------------------------------------+") 