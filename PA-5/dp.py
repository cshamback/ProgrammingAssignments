from task import *
from merge import *

# prints dictionary of tasks as lists separated by arrows
def printTasks(memo):
    for key in memo: 
        # a single profit can have multiple task lists, iterate thru them all 
        for taskList in memo[key]:
            print(" " + " -> ".join(taskList), end="")
            print(" with a total earning of " + str(key) + ".")
            print()

    print()

# checks if the start or end times overlap, returns bool
def overlaps(t1, t2): 
    # 3 cases for overlap: they start at the same time, t1 starts in the middle of t2, t1 ends in the middle of t2
    return (t1.start == t2.start) or (t1.start > t2.start and t1.start < t2.end) or (t1.end > t2.start and t1.end < t2.end)

def dp(tasks):# tasks is an array of Task objects
    memo = {} # key = profit, value = list of tasks leading to profit 

    # store list of tasks in memo where key = profit and value = [[task]]
    # each of these is a starting point for a list of tasks, and multiple lists for a single profit is possible
    # we will later get rid of lists that are subsets of other lists 
    for task in tasks:
        if task.pay not in memo: 
            memo[task.pay] = []
        memo[task.pay].append([task.name])

    # printTasks(memo)
    
    for i in range(1, len(tasks)): #  iterates thru all keys. can get values associated using memo[key]
        j = 0
        while(j < i):
            # if the two tasks do NOT overlap, we can put them together. 
            if(overlaps(tasks[i], tasks[j]) == False):
                
                # we found a new profit, so it needs a new entry in memo. 
                newKey = tasks[j].pay + tasks[i].pay

                # copy existing sequences at previous pay into a new array
                # seq = iterate thru all lists associated with key, append to taskLists one at a time
                taskLists = [seq + [tasks[j].name] for seq in memo.get(tasks[i].pay, [])]

                # append old task list back to memo[newKey]
                if newKey not in memo:
                    memo[newKey] = []

                memo[newKey].extend(taskLists)

                # if the pair of tasks does not result in higher profit, ignore 
            j = j + 1

    # return value of max key in memo
    maxPay = max(memo)

    # print all task lists that fit this profit
    print("All possible sets of tasks are: ")
    printTasks(memo)     
    print()       

    # return 2d array of task lists that have max profit
    return memo[maxPay]

tasks = [Task(30, 0, 3, "Task 1"), Task(30, 0, 4, "Task 2"), Task(10, 1, 2, "Task 3"), Task(1, 4, 6, "Task 4"), Task(5, 7, 10, "Task 5"), Task(6, 9, 11, "Task 6")]
dp(tasks)