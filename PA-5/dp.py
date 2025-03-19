from task import *
from merge import *

# prints dictionary of tasks as lists separated by arrows
def printTasks(memo):
    for key in memo: 
        print("Profit = " + str(key), end=": ")
        listAsStr = " -> ".join(memo[key])
        print(listAsStr)
    print()

def dp(tasks):
    memo = {} # key = profit, value = list of tasks leading to profit 

    # store list of tasks in memo where key = profit and value = [task]
    for task in tasks:
        memo[task.pay] = [task.name]
    printTasks(memo)

    # return value of max key in memo

tasks = [Task(30, 0, 3, "Task 1"), Task(30, -1, 4, "Task 2"), Task(10, 1, 2, "Task 3"), Task(1, 4, 6, "Task 4"), Task(5, 7, 10, "Task 5"), Task(6, 9, 11, "Task 6")]
dp(tasks)