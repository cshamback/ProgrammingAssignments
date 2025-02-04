#Recursion
def Fib(count):
    previous_term = 1
    current_term = 0
    next_term = 0

    for i in range(count):
        next_term = current_term + previous_term
        current_term = previous_term
        previous_term = next_term   
    return current_term

for i in range(10):
    print(Fib(i))

#First Iteration/Attempt at a fibonacci sequence, it works. All that's left is to make this recursive.