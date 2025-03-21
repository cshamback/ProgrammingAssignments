#Custom Alg to find all valid schedules maximizing the number of tasks using dynamic programming

def find_max_sets(tasks):
    tasks.sort(key=lambda x: x.end) #sort tasks by end time
    n = len(tasks)

    #initialize dp table where dp[i] stores (max task count, list of valid schedules)
    dp = [(0, []) for _ in range(n)]

    for i in range(n):
        #initialize max task count and valid schedules
        max_count = 1
        best_schedules = [[tasks[i]]]

        for j in range(i):
            #if task j is compatible with task i
            if tasks[j].end <= tasks[i].start: # Non-overlapping tasks
                #if task j can be added to the schedule
                if dp[j][0] + 1 > max_count:
                    max_count = dp[j][0] + 1
                    best_schedules = [schedule + [tasks[i]] for schedule in dp[j][1]]
                #if task j cannot be added to the schedule
                elif dp[j][0] + 1 == max_count:
                    best_schedules.extend(schedule + [tasks[i]] for schedule in dp[j][1])

        dp[i] = (max_count, best_schedules)

    #find the schedule with the maximum number of tasks
    max_task_count = max(dp, key=lambda x: x[0])[0]
    all_schedules = [schedule for count, schedules in dp for schedule in schedules if count == max_task_count]

    print(all_schedules)

    # Remove subsets efficiently
    filtered_schedules = []
    for schedule in all_schedules:
        schedule_set = set((task.pay, task.start, task.end, task.name) for task in schedule)

        if not any(set(other_schedule).issubset(schedule_set) for other_schedule in all_schedules if other_schedule != schedule):
            filtered_schedules.append(schedule)

    return filtered_schedules