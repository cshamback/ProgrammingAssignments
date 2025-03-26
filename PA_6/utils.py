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
