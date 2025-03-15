import time
from functools import lru_cache
Stops = []
def get_user_input():
    numSteps = 0 
    print("* * * * * * * * * * * * * * * * * * * *")
    print("  P-A-4:  S T A I R  C O U N T I N G ")
    print("* * * * * * * * * * * * * * * * * * * *")

    validInput = False 
    while not validInput:
        numSteps = int(input("Please enter the number of steps in the staircase: "))
        if numSteps < 2:
            print("Invalid. Please enter a number of steps that is at least 2.")
        else:
            validInput = True

    print("\nPlease enter the number of steps allowed per leap as a series of integers separated by spaces.")
    print(f"You must enter at least two numbers. If you enter a number larger than {numSteps} or smaller than 1, it will be ignored.")

    validInput = False 
    stepsAllowed = []
    while not validInput:
        temp = input(" ")
        stepsAllowed = [int(num) for num in temp.split(" ") if 1 <= int(num) <= numSteps]
        stepsAllowed = list(set(stepsAllowed))
        
        if len(stepsAllowed) < 2 or len(stepsAllowed) > numSteps:
            print(f"You may only enter a number of leaps that is between 2 and {numSteps} inclusive.")
        else:
            validInput = True

    print(f"Valid input accepted. Number of steps: {numSteps}, Leaps allowed: {stepsAllowed}\n")
    Stops = stepsAllowed
    return numSteps, stepsAllowed

def count_ways_dp(n, steps):
    dp = [0] * (n + 1)
    dp[0] = 1
    
    for i in range(1, n + 1):
        for step in steps:
            if i - step >= 0:
                dp[i] += dp[i - step]
    
    return dp[n]

@lru_cache
def count_ways_rc(n, steps):
    #initial conditions of the recursion. Ideally, we'd use 1 and 2 but it can work on any number
    # as long as it's not bigger than stepsStaircase
    n1 = steps[0]
    n2 = steps[1]
    
    # in case something inputs 0
    if(n == 0):
        return 1
    if(n < 0):
        return 0
    
    # recursion using the initial conditions
    return count_ways_rc(n - n1, steps) + count_ways_rc(n - n2, steps)

def generate_paths(n, steps, path=[], paths=[]):
    if n == 0:
        paths.append(" -> ".join(map(str, path)))
        return
    
    for step in steps:
        if n - step >= 0:
            generate_paths(n - step, steps, path + [step], paths)
    
    return paths

def main():
    n, allowed_steps = get_user_input()
    allowed_steps.sort()
    
    start_time_dp = time.time()
    total_ways_dp = count_ways_dp(n, allowed_steps)
    dp_time = time.time() - start_time_dp
    
    paths = generate_paths(n, allowed_steps, path=[], paths=[])
    
    print(f"The time elapsed in the non-recursive algorithm is {dp_time:.6f} seconds.")
    print(f"There are a total of {total_ways_dp} ways.")
    for i, way in enumerate(paths, 1):
        print(f"Way {i}: {way}")
    #------------------------------------------------------
    start_time_rc = time.time()
    total_ways_rc = count_ways_rc(n, tuple(allowed_steps))
    rc_time = time.time() - start_time_rc
    paths_rc = generate_paths(n, allowed_steps, path=[], paths=[])
    
    print(f"The time elapsed in the recursive algorithm is {rc_time:.6f} seconds.")
    print(f"There are a total of {total_ways_rc} ways.")
    for i, way in enumerate(paths_rc, 1):
        print(f"Way {i}: {way}")

if __name__ == "__main__":
    main()