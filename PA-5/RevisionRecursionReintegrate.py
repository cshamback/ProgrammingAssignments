from task import *
from merge import *
from bf import *

# RECREATION OF EVERYTHING FOR TESTING STUFF
tasks = [Task(30, 0, 3, "Task 1"), Task(30, -1, 4, "Task 2"), Task(10, 1, 2, "Task 3"), Task(1, 4, 6, "Task 4"), Task(5, 7, 10, "Task 5"), Task(6, 9, 11, "Task 6")]

def RecursiveDP(taskQueue):
    memo = {}  # Initialize a fresh dictionary
    def confidenceChecks(listIndex):
        if listIndex >= len(taskQueue):
            return 0
    
        # Check if already calculated this index
        if listIndex in memo:
            return memo[listIndex]
        
        currentTask = taskQueue[listIndex]
        
        
        keptProfit = currentTask.pay + confidenceChecks(listIndex + 1)
        memo[listIndex] = currentTask, keptProfit
        
        
        print(currentTask)
        
        return keptProfit
    return confidenceChecks(0)

print(f"Total Profit: {RecursiveDP(tasks)}")