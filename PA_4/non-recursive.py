import time

def get_user_input():
    numSteps = 0 
    print("* * * * * * * * * * * * * * * * * * * *")
    print("  P-A-4: D Y N A M I C  S T A I R S ")
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
    return numSteps, stepsAllowed

def count_ways_dp(n, steps):
    dp = [0] * (n + 1)
    dp[0] = 1
    
    for i in range(1, n + 1):
        for step in steps:
            if i - step >= 0:
                dp[i] += dp[i - step]
    
    return dp[n]

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
    
    start_time = time.time()
    total_ways_dp = count_ways_dp(n, allowed_steps)
    dp_time = time.time() - start_time
    
    paths = generate_paths(n, allowed_steps, path=[], paths=[])
    
    print(f"The time elapsed in the non-recursive algorithm is {dp_time:.6f} seconds.")
    print(f"There are a total of {total_ways_dp} ways.")
    for i, way in enumerate(paths, 1):
        print(f"Way {i}: {way}")

if __name__ == "__main__":
    main()