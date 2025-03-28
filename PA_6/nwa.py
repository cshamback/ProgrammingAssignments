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

def get_all_alignments(matrix, seq1, seq2, match, mismatch, gap):
    """
    Recursively finds all optimal alignments from the DP matrix.

    Returns:
        alignments (list of tuples): List of (aligned_seq1, aligned_seq2)
    """
    alignments = []

    def traceback(i, j, aligned1, aligned2):
        if i == 0 and j == 0:
            alignments.append((aligned1[::-1], aligned2[::-1]))
            return

        # Diagonal move: match or mismatch
        if i > 0 and j > 0:
            score = match if seq1[j-1] == seq2[i-1] else mismatch
            if 0 <= i-1 < len(matrix) and 0 <= j-1 < len(matrix[0]):
                if matrix[i][j] == matrix[i-1][j-1] + score:
                    traceback(i-1, j-1, aligned1 + seq1[j-1], aligned2 + seq2[i-1])

        # Up move: gap in seq1
        if i > 0 and matrix[i][j] == matrix[i-1][j] + gap:
            traceback(i-1, j, aligned1 + "-", aligned2 + seq2[i-1])

        # Left move: gap in seq2
        if j > 0 and matrix[i][j] == matrix[i][j-1] + gap:
            traceback(i, j-1, aligned1 + seq1[j-1], aligned2 + "-")

    traceback(len(seq2), len(seq1), "", "")
    return alignments

def print_alignments(alignments, score):
    print("\nAll Optimal Alignments:")
    for a1, a2 in alignments:
        # Build a visual match line
        match_line = ""
        for c1, c2 in zip(a1, a2):
            if c1 == c2:
                match_line += "|"
            elif c1 == "-" or c2 == "-":
                match_line += " "
            else:
                match_line += "."

        # Print the alignment
        print(a1)
        print(match_line)
        print(a2)
        print(f"Score: {score}")
        print()

