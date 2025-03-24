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
