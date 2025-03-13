numSteps = 0 

print("* * * * * * * * * * * * * * * * * * * *")
print("  P-A-4: D Y N A M I C  S T A I R S ")
print("* * * * * * * * * * * * * * * * * * * *")

# get number of steps and validate input - must be at least 2.
# there must be at least two leaps that are greater than 0 steps.
# but no leap can be greater than the number of steps. if there is only 1 step, 
# the only leap that can happen is 1 step. 
# this is not a valid input, so we can't let the user do it. 

validInput = False # flag var

while(validInput == False):
    numSteps = int(input("Please enter the number of steps in the staircase: "))
    if (numSteps < 2):
      print("Invalid. Please enter a number of steps that is at least 2.")
    else: 
      validInput = True; 

# get number of steps per leap
# must be between [2, numSteps] and must have [2, numSteps] members

print("")
print("Please enter the number of steps allowed per leap as a series of integers separated by spaces. For example, 1 3 4 5.")
print("You must enter at least two numbers. If you enter a number larger than " + str(numSteps) + " or smaller than 1, it will be ignored.")

validInput = False # flag var
stepsAllowed = [] # will be filled inside while loop 

while(validInput == False):
    temp = input(" ")
    
    # turn user input string into array for use 
    stepsAllowed = [int(num) for num in temp.split(" ")]
    print("Steps allowed: " + str(stepsAllowed))

    # remove duplicates 
    stepsAllowed = list(set(stepsAllowed))

    # delete any numbers greater than numSteps
    # does not actually change the flag 
    for i in range(0, len(stepsAllowed)):
        if (stepsAllowed[i] > numSteps or stepsAllowed[i] < 1):
            print("Invalid leap found: " + str(stepsAllowed[i]) + " will be removed.")
            del stepsAllowed[i]

    print("Your input with only valid values: " + str(stepsAllowed))

    # check that a valid number of allowed steps has been given        
    if(len(stepsAllowed) < 2 or len(stepsAllowed) > numSteps):
       print("You may only enter a number of leaps that is between 2 and " + str(numSteps) + " inclusive.")
       print("You have entered " + str(len(stepsAllowed)) + " leaps. Please re-enter a valid set of leaps:")
    else: 
       validInput = True # breaks while loop 

print("Valid input accepted. number of steps: " + str(numSteps) + " leaps allowed: " + str(stepsAllowed))
print("")
