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