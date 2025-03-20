#brute force alg
import time
from itertools import combinations
from task import Task
from merge import mergeSort

def is_valid_schedule(tasks):
    """Check if a given subset of tasks has overlapping times."""
    tasks = sorted(tasks, key=lambda x: x.end)  # Sort by end time
    for i in range(len(tasks) - 1):
        if tasks[i].end > tasks[i + 1].start:  # Check if end time of one task overlaps with start time of another
            return False
    return True

def brute_force_maximize_earnings(tasks):
    """Brute-force approach to find the best schedule maximizing earnings."""
    max_earning = 0
    best_schedules = []
    
    # Generate all possible subsets of tasks
    for r in range(1, len(tasks) + 1):
        for subset in combinations(tasks, r):
            if is_valid_schedule(subset):
                earning = sum(task.pay for task in subset)
                if earning > max_earning:
                    max_earning = earning
                    best_schedules = [subset]
                elif earning == max_earning:
                    best_schedules.append(subset)
    
    return best_schedules, max_earning

def main():
    # Get user input
    numTasks = int(input("Enter the number of all paid tasks: "))
    tasks = []
    
    for i in range(numTasks):
        currEarning = int(input("Enter the amount earned by task " + str(i + 1) + ": "))
        currStart = int(input("Enter the start time of the task: "))
        currEnd = int(input("Enter the end time of the task: "))
        tasks.append(Task(currEarning, currStart, currEnd, "Task " + str(i + 1)))

    
    # Sort tasks by end time
    tasks = mergeSort(0, len(tasks) - 1, tasks)
    
    # Measure brute-force execution time
    start_time = time.time()
    best_schedules, max_earning = brute_force_maximize_earnings(tasks)
    elapsed_time = time.time() - start_time
    
    # Display results
    print("\nThe time elapsed in the brute-force algorithm is {:.6f} ms.".format(elapsed_time * 1000))
    print("Maximum Earning: {}\n".format(max_earning))
    
    print("There are {} options to select different sets of tasks.".format(len(best_schedules)))
    for idx, schedule in enumerate(best_schedules, 1):
        task_order = " -> ".join(task.name for task in schedule)
        print("Option {}: {}, with a total earning of {}".format(idx, task_order, max_earning))   

if __name__ == "__main__":
    main()
