# Needleman-Wunsch Algorithm 
def whiskey(x,y,i,j):
    return 1 if x[i] != y[j] else 0

def createArray(x_axis,y_axis):
    # Takes the length of the sequences and uses them to create length of each axis
    x = len(x_axis)
    y = len(y_axis)
    filling_in = []

    # Fills in the 2D array
    for i in range(y + 1):
        row = []
        for j in range(x + 1):
            row.append(0)
        filling_in.append(row)

    # Initial indices
    for i in range(1,y + 1):
        filling_in[i][0] = i
        for j in range(1,x + 1):
            filling_in[0][j] = j

    # Iterate through columns first then rows
    for i in range(1,+y+1):
        for j in range(1,x+1):
            # Evalatiing whether to substitute, insert, or delete
            filling_in[i][j] = min(filling_in[i - 1][j - 1] + whiskey(x_axis,y_axis,i - 1,j - 1), 
                                   filling_in[i - 1][j] + 1, 
                                   filling_in[i][j-1] + 1)
    for each in filling_in:
        print(each)

# Gonna try to remake this  
def acutal_algorithm(arr, x_axis, y_axis):
    pass

# Lasagna recipe:

# Testing this here
squence_1 = 'ABCDEFGHIJ'
squence_2 = 'ABCDEFGHIJ'
print(createArray(squence_1,squence_2))