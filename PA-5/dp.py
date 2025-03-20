from task import *
from merge import *

from collections import defaultdict

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
def removeSubsets(memo):
    # convert each value (2d array) to a list of frozen sets
    # frozen sets are sets that cannot be modified
    memoSets = {key: [frozenset(sublist) for sublist in value] for key, value in memo.items()}

    # separates task lists from their 2d array
    # unique tasks are used as keys; keys are used as values so there can be multiple keys 
    setDict = defaultdict(set)
    for key, sets in memoSets.items():
        for s in sets:
            setDict[s].add(key)
    
    # remove subsets
    uniqueSets = list(setDict.keys()) # one large list containing every task list represented as a frozenset
                                      # ie.[frozenset({"Task 1"}), frozenset({"Task 2"})...]
    toRemove = set() # can't delete while iterating through array, so store values to be deleted for later

    for i, s1 in enumerate(uniqueSets):
        for j, s2 in enumerate(uniqueSets):

            # in python, the "<" operator between two sets (such as s1 < s2)
            # checks if s1 is a proper subset of s2 (s1 contains all elements in s2, and s2 contains at least 1 extra element)
            if i != j and s1 < s2:
                toRemove.add(s1)

    # remove toRemove items from memo
    cleanMemo = {}

    # iterate through all of setDict
    for key, sets in setDict.items(): # key = unique set, value = that set's profit
        memoKey = sets.pop()
        if(key not in toRemove):
            if(memoKey not in cleanMemo):
                cleanMemo[memoKey] = []

            cleanMemo[memoKey].append(key)

    return cleanMemo

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
                    # make sure we're not adding duplicates to taskList
                    if [tasks[j].name] not in seq and [tasks[j].name] + seq not in seq:
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
    memo = removeSubsets(memo)

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