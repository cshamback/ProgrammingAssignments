from task import *
from merge import *

def addToMemo(task, memo):
    temp = []
    temp.append(task)
    memo.append(temp)

def printTasks(memo): 
    for row in range(len(memo)): 
        for col in range(len(memo[row])):
            if(col == len(memo[row]) - 1):
                print(memo[row][col].name) # print the last task in the arr without an arrow
            else:
                print(memo[row][col].name , end=" -> ") # print all on the same line, followed by an arrow symbol
        print()

def dp(tasks):
    # INITIALIZATION ------------------------------------------------------------
    memo = [] # 2d array that cont ains all lists of tasks - array of subtasks

    # merge sort all tasks by end time
    temp = []
    temp = mergeSort(0, len(tasks), tasks)
    tasks = temp

    # ADD ALL STARTING POINTS TO MEMO --------------------------------------------
    # cannot start at any task, must be the first one or one that overlaps with it 
    addToMemo(tasks[0], memo)

    for i in range(1, len(tasks)):
        if((tasks[i].start < tasks[0].start) or (tasks[i].end < tasks[0].end)):
            addToMemo(tasks[i], memo)

    printTasks(memo)

    # FINISHED: RETURN MEMO SO IT CAN BE USED/PRINTED --------------------------
    return memo

tasks = [Task(30, 0, 3, "Task 1"), Task(30, -1, 4, "Task 2"), Task(10, 1, 2, "Task 3"), Task(1, 4, 6, "Task 4"), Task(5, 7, 10, "Task 5"), Task(6, 9, 11, "Task 6")]
results = dp(tasks)
printTasks(results)