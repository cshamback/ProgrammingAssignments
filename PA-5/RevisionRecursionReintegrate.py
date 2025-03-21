from task import *
from merge import *
from bf import *

def RecursiveDP(taskQueue):
    memo = {}  # Store max profits at each index
    memoPath = {}  # Store the best paths for each index
    allPaths = []  # Store all possible valid paths

    def computeProfit(listIndex, selectedTasks=[]):  # Pass selectedTasks to track conflicts
        if listIndex >= len(taskQueue):  # Base case: end of the list
            return 0, []

        if listIndex in memo:  # Use memoization if result is already computed
            return memo[listIndex], memoPath[listIndex]
        
        currentTask = taskQueue[listIndex]

        # Option 1: Skip the current task
        skipProfit, skipPath = computeProfit(listIndex + 1, selectedTasks)

        # Option 2: Take the current task (if no conflicts)
        takeProfit = currentTask.pay
        nextCompatibleTask = listIndex + 1

        # Find the next **truly non-overlapping** task
        while nextCompatibleTask < len(taskQueue) and taskQueue[nextCompatibleTask].start < currentTask.end:
            nextCompatibleTask += 1

        # Ensure the selected task does not overlap with any previously selected task
        if all(task.end <= currentTask.start or task.start >= currentTask.end for task in selectedTasks):
            takeProfit += computeProfit(nextCompatibleTask, selectedTasks + [currentTask])[0]
            bestPath = [currentTask] + computeProfit(nextCompatibleTask, selectedTasks + [currentTask])[1]
        else:
            takeProfit = -1  # Invalidate this path so it doesn't get selected
            bestPath = []

        # Choose the better option (max profit)
        if takeProfit > skipProfit:
            bestProfit = takeProfit
        else:
            bestProfit = skipProfit
            bestPath = skipPath

        # Store results in memoization tables
        memo[listIndex] = bestProfit
        memoPath[listIndex] = bestPath

        # Ensure unique, valid paths in allPaths
        if (bestPath, bestProfit) not in allPaths and bestProfit != -1:
            allPaths.append((bestPath, bestProfit))

        return bestProfit, bestPath

    # Compute the maximum profit schedule
    max_profit, path = computeProfit(0)

    # Sort all valid schedules by earnings in descending order
    allPaths.sort(key=lambda x: x[1], reverse=True)

    return allPaths, max_profit



"""
# Denny's Breakfast Bribes
profits, Evaluated = RecursiveDP(tasks)

for path, earnings in profits:
    task_names = " -> ".join([task.name for task in path])
    print(f"{task_names} with a total earning of {earnings}.")
print(f"Max profit is {Evaluated}")"
"""