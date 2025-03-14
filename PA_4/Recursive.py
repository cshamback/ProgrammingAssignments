import time
#
stepsStaircase = int(input("How many steps are in the staircase? "))
initialConditions =[]
for i in range (2):
    initialConditions.append(int(input("How many steps can you take up at a time? ")))

def count_ways_rc(n):
    n1 = initialConditions[0]
    n2 = initialConditions[1]
    
    if(n == 0):
        return 1
    if(n < 0):
        return 0
    
    return count_ways_rc(n - n1) + count_ways_rc(n - n2)

print(f"There are a total of {count_ways_rc(stepsStaircase)}")

