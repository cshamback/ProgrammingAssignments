# Attempting to make my own alg for the problem
# parameters: dna1 first dna sequence (goes across the top), dna2 second dna sequence (goes down the side), 
# match score, mismatch score (penalty for mismatch), gap score (penalty for gap)
# dna sequences are strings
# scores are integers

def initialize_matrix(dna1, dna2, match, mismatch, gap):
    rows = len(dna2) + 1
    cols = len(dna1) + 1

    matrix = [[0 for _ in range(cols)] for _ in range(rows)] # creates matrix of zeros as a 2d list

    # initialize first column
    for i in range(1, rows):
        matrix[i][0] = matrix[i-1][0] + gap
    
    # initialize first row
    for j in range(1, cols):
        matrix[0][j] = matrix[0][j-1] + gap

    # Fill in the rest of the matrix
    # Each cell [i][j] considers 3 possible ways to arrive there:
    #   - from the top (gap in dna1)
    #   - from the left (gap in dna2)
    #   - from the top-left diagonal (match or mismatch)
    for i in range(1,rows):
        for j in range(1,cols):
            # Check the characters we're comparing: seq1[j-1] (horizontal), seq2[i-1] (vertical)
            if dna1[j - 1] == dna2[i - 1]:
                #the characters match add the match score to diagonal move
                diag_score = matrix[i - 1][j - 1] + match
            else:
                #the characters don't match add the mismatch score to diagonal move
                diag_score = matrix[i - 1][j - 1] + mismatch

            # Add gap penalty to vertical and horizontal moves
            vert_score = matrix[i - 1][j] + gap
            horiz_score = matrix[i][j - 1] + gap

            matrix[i][j] = max(diag_score, vert_score, horiz_score)
        
    return matrix