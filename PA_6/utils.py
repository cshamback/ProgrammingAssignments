# INPUT 

# get a valid string of valid chars from user 
def getValidString(validChars):
    flag = True

    while(flag):
        # make sure what was entered only contains ACGT, -, and _
        # if both are sets and their difference is an empty set, it is valid 
        seq1 = input("").upper()
        seqSet = set(seq1)

        if(seqSet - validChars == set()):
            flag = False
        else: 
            print("Sequence contains at least one invalid character. Please try again.")

    return seq1

# TRACEBACK CHART

# goal: starting at bottom right, iterate through every cell in the output chart. 
# for each cell, print it plus an arrow pointing to the cell (i-1, j; i - 1, j - 1, or i, j - 1) that maximizes its score

# arr is the 2d arr that we're making a traceback for

def findTraceback(arr):
    chart = [[] for _ in range(len(arr))] # create a blank 2d arr with the same number of rows as arr

    # row 0 has no arrows, just numbers - insert those; leave spaces for arrows
    for i in range(len(arr[0]) - 1, 0, -1): # iterate backwards so we can prepend easier
        chart[0].insert(0, str(arr[0][i]))
        chart[0].insert(0, " ")

    print(chart)

    # iterate thru input arr - ignoring first row and first col
    for row in range(len(arr) - 1, 0, -1): # all rows except first one
        for col in range(len(arr[row]) - 1, 0, -1): # all cols except first one
            bestAdj = getMaxAdjacent(arr, row, col)

            # add an arrow to the chart to the left of arr[row][col] that points toward bestAdj
            # [[arrow], reward] goes in same row, gets prepended to that row (first col)

            # figure out what arrow to use, order: (row, col)
            currArrow = " "
            if bestAdj[1] == col - 1: # left of current
                if bestAdj[0] == row - 1: # also above current
                    currArrow = "⭦ "
                else: # left but not above 
                    currArrow = "⭠ "
            else: # above current
                currArrow =  "⭡ "

            chart[row].insert(0, arr[row][col])
            chart[row].insert(0, currArrow)

            print(f"Current arrow: {currArrow} Current score: {arr[row][col]}")
                
    print(chart)
    return chart

# returns tuple of row and column of adjacent highest score to input cell (row, col)
# can only go left, up, or up and left, find max of all 3. 

# arr is the 2d array of scores already calculated
# row and col are the indexes of a cell to find the arrow for 

def getMaxAdjacent(arr, row, col):
    adjRow = 0
    adjCol = 0

    adjacent = [[row - 1, col], [row, col - 1], [row - 1, col - 1]]
    maxScore = float('-inf')

    for i in range(len(adjacent)):
        # get reward/penalty associated with tuple in adjacent 
        score = arr[adjacent[i][0]][adjacent[i][1]] # always 2 vals in each row, 1st is row and 2nd is col
        
        # compare what was found to current max
        if score > maxScore: 
            maxScore = score
            adjRow = adjacent[i][0]
            adjCol = adjacent[i][1]

    print(f"Max adjacent score for {row},{col}, score = {arr[row][col]} is: {adjRow}, {adjCol}")

    return (adjRow, adjCol)

def print_matrix(matrix, seq1, seq2):
#Pretty prints the scoring matrix with sequence labels.
#seq1 goes across the top (columns), seq2 goes down the side (rows).
    cols = len(seq1)
    rows = len(seq2)

    # Print header row
    print("    ", end="")
    print("    ", end="")  # top-left corner empty cell
    for char in seq1:
        print(f"{char:>4}", end="")
    print()

    # Print each row with row label
    for i in range(len(matrix)):
        if i == 0:
            print("    ", end="")  # first empty row label
        else:
            print(f"{seq2[i - 1]:>4}", end="")

        for j in range(len(matrix[0])):
            print(f"{matrix[i][j]:>4}", end="")
        print()


#FOR TESTING: uncomment to test getMaxAdjacent()
sample = [[0, -1, -2, -3, -4],[-1, 4, 6, 7, 7],[-2, 4, 6, 9, 9],[-3, 7, 6, 5, 10], [-4, 10, 19, 5, 6]]
print_matrix(sample, "AAAA", "AAAA")
getMaxAdjacent(sample, 2, 4)
getMaxAdjacent(sample, 1, 1)
getMaxAdjacent(sample, 4, 4)
getMaxAdjacent(sample, 1, 3)

traceback = findTraceback(sample)
print(traceback)
print_matrix(traceback, "AAAA", "AAAA")