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

def countTaskLists(memo):
    count = 0
    for key in memo: 
        for taskList in memo[key]:
            count += 1
    return count 

# checks if the start or end times overlap, returns bool
def overlaps(t1, t2): 
    # 3 cases for overlap: they start at the same time, t1 starts in the middle of t2, t1 ends in the middle of t2
    return (t1.start == t2.start) or (t1.start > t2.start and t1.start < t2.end) or (t1.end > t2.start and t1.end < t2.end)

# given a 2d array and a list, remove all subsets of the list from the 2d array
def removeSubsets(memo, newArr):
    newSet = set(newArr)

    for key in list(memo.keys()):
        # set memo[key] to only contain sequences that are not subsets of a given set
        memo[key] = [seq for seq in memo[key] if not set(seq).issubset(newSet)]

        # if there are no more values associated with the key, delete it 
        if memo[key] == None:
            del memo[key]

# iterate through every arr in existing arrs and determine if new arr is a subset of any of them 
def isSubset(newArr, existingArrs):
    newSet = set(newArr)

    for arr in existingArrs: 
        if(newSet.issubset(set(arr))):
            print("Found subset. " + str(arr) + " is a subset of " + str(newSet))
            return True
        else: 
            print(str(arr) + " is not a subset of " + str(newSet))
        
    return False 

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

                # list of all new sequences created by adding tasks[j] to all sequences in memo.get(key)
                taskList = []
                for seq in memo.get(tasks[i].pay, []):
                    if [tasks[j].name] not in seq:
                        taskList.append([tasks[j].name] + seq)

                if(newKey not in memo):
                    memo[newKey] = []

                memo[newKey].extend(taskList)

                # if the pair of tasks does not result in higher profit, ignore 
            j = j + 1

    # remove subsets
    # if a task has a subset anywhere in memo, delete that subset. 

    # we want to iterate thru the keys in descending order. 
    # most likely, the highest profits will have the most tasks associated with them. 
    # this means more subsets will be elimated and we'll search less of the dict 
    
    keys = list(memo.keys())
    keys.sort()
    keys.reverse()
    print(keys)

    # return value of max key in memo
    maxPay = max(memo)

    # print all task lists that fit this profit
    print("There are " + str(countTaskLists(memo)) + " options to select different sets of tasks.")
    printTasks(memo)     
    print()       

    # return 2d array of task lists that have max profit
    return memo[maxPay]

tasks = [Task(30, 0, 3, "Task 1"), Task(30, 0, 4, "Task 2"), Task(10, 1, 2, "Task 3"), Task(1, 4, 6, "Task 4"), Task(5, 7, 10, "Task 5"), Task(6, 9, 11, "Task 6")]
dp(tasks)