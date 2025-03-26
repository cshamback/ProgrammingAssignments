import numpy as np

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

<<<<<<< HEAD
# TRACEBACK CHART

# goal: starting at bottom right, iterate through every cell in the output chart. 
# for each cell, print it plus an arrow pointing to the cell (i-1, j; i - 1, j - 1, or i, j - 1) that maximizes its score

# arr is the 2d arr that we're making a traceback for

def findTraceback(arr):
    arrows = ["⭦", "⭡", "⭠ "] # used to print traceback chart
    chart = list(np.zeros_like(np.array(arr))) # create a blank 2d arr with the same number of spaces as arr

    # iterate thru input arr
     
    return chart

# returns tuple of row and column of adjacent highest score to input cell (row, col)
# can only go left, up, or up and left, find max of all 3. 
def getAdjacent(arr, row, col):
    adjRow = 0
    adjCol = 0
    return (adjRow, adjCol)
=======
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
>>>>>>> ec3155d9942bda3146dc6a226ed36eb027a8a8b3
