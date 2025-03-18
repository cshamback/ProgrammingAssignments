from task import *
from merge import *

def addToMemo(task, memo):
    temp = []
    temp.append(task)
    memo.append(temp)

# prints 2d array of tasks
def printTasks(memo): 
    for row in range(len(memo)): 
        for col in range(len(memo[row])):
            if(col == len(memo[row]) - 1):
                print(memo[row][col].name) # print the last task in the arr without an arrow
            else:
                print(memo[row][col].name , end=" -> ") # print all on the same line, followed by an arrow symbol
        print()

# prints list of task names 
def printSingleList(arr):
    for i in range(len(arr)):
        if(i == len(arr) - 1):
            print(arr[i].name)
        else:
            print(arr[i].name, end=" -> ")

def dp(tasks):
    memo = [[]]
    return memo

tasks = [Task(30, 0, 3, "Task 1"), Task(30, -1, 4, "Task 2"), Task(10, 1, 2, "Task 3"), Task(1, 4, 6, "Task 4"), Task(5, 7, 10, "Task 5"), Task(6, 9, 11, "Task 6")]
results = dp(tasks)
printTasks(results)