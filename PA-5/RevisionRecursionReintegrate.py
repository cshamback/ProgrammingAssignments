from task import *
from merge import *
from bf import *

# RECREATION OF EVERYTHING FOR TESTING STUFF
tasks = [Task(3000, 0, 3, "Task 1"), Task(30, -1, 4, "Task 2"), Task(10, 1, 2, "Task 3"), Task(1, 4, 6, "Task 4"), Task(5, 7, 10, "Task 5"), Task(6, 9, 11, "Task 6")]

def RecursiveDP(taskQueue):
    memo = {}  # Initialize a dictionary for profits
    memoPath = {}  # Initialize a dictionary for paths
    allPaths = []  # Stores all possible paths with their earnings
    

    # Computes the best path to get the highest profits
    def computeProfit(listIndex):
        # checks the indices themselves for a set length compared to the queue
        if listIndex >= len(taskQueue):
            return 0, []  
        
        # Check if already calculated this index, otherwise make it the current task
        if listIndex in memo:
            return memo[listIndex], memoPath[listIndex]
        else:
            currentTask = taskQueue[listIndex]
    
        # Tell it to move on, it's had enough
        skipProfit, skipPath = computeProfit(listIndex + 1)
        
        # Define the current task's pay and move on
        takeProfit = currentTask.pay
        nextCompatibleTask = listIndex + 1
        
        # Looking ahead for other tasks 
        while nextCompatibleTask < len(taskQueue) and taskQueue[nextCompatibleTask].start < currentTask.end:
            nextCompatibleTask += 1
        
        # Add profit of the next task to the original
        takeProfit += computeProfit(nextCompatibleTask)[0]
        
        # Determine which option is better
        if takeProfit > skipProfit:
            bestProfit = takeProfit
            bestPath = [currentTask] + computeProfit(nextCompatibleTask)[1]  # Include current task in path
        else:
            bestProfit = skipProfit
            bestPath = skipPath
        
        # Memoize the result and path for this index
        memo[listIndex] = bestProfit
        memoPath[listIndex] = bestPath
        
        # Checks if the certain path is in allPaths. If not, add it!
        if (bestPath, bestProfit) not in allPaths:
            allPaths.append((bestPath, bestProfit))

        
        return bestProfit, bestPath
    
    # Call the function again
    max_profit, path = computeProfit(0)
    
    # Sort all paths by total earnings in descending order
    allPaths.sort(key=lambda x: x[1], reverse=True)
    
    return allPaths, max_profit

# Denny's Breakfast Bribes
profits, Evaluated = RecursiveDP(tasks)

for path, earnings in profits:
    task_names = " -> ".join([task.name for task in path])
    print(f"{task_names} with a total earning of {earnings}.")
print(f"Max profit is {Evaluated}")