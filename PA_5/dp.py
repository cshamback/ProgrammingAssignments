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

def countTaskLists(memo):
    count = 0
    for key in memo: 
        for taskList in memo[key]:
            count += 1
    return count 

# checks if the start or end times overlap, returns bool
def overlaps(t1, t2): 
    # overlap if t1 starts in the middle of t2, or t1 ends in the middle of t2
    return (t1.start < t2.start and t2.start < t1.end) or (t1.start < t2.end and t2.end < t1.end)

# given a 2d array and a list, remove all subsets of the list from the 2d array
def removeSubsets(memo):
    # convert each value (2d array) to a list of frozen sets
    # frozen sets are sets that cannot be modified
    memoSets = {key: [frozenset(sublist) for sublist in value] for key, value in memo.items()}
    print(memoSets)

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

def dp(tasks): # tasks is an array of Task objects
    
    T = [None] * len(tasks)
    T[0] = tasks[0].pay
    
    # examine every task - already in order by end time 
    for i in range(1, len(tasks)): #  iterates thru all keys. can get values associated using memo[key]
        
        # add profit of i by itself to array of profits
        T[i] = max(tasks[i].pay, T[i - 1])
        
        # examine every task that ends before task i in reverse order (closest to i first)
        j = i - 1
        while(j >= 0):
            # only care about adding new tasks that don't overlap with task i 
            if(tasks[j].end <= tasks[i].start):
                T[i] = max(T[i], tasks[i].pay + T[j])

            j -= 1

    maxProfit = -1
    for val in T:
        if(maxProfit < val):
            maxProfit = val

    return maxProfit