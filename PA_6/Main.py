# MAIN
from utils import *
from nwa import initialize_matrix

print("* * * * * * * * * * * * * * * * * * * * * * * * * * * * * * *")
print("* P A 6  N E E D L E M A N - W U N S C H  A L G O R I T H M *")
print("* * * * * * * * * * * * * * * * * * * * * * * * * * * * * * *")
print()

print("Please enter the first DNA sequence.") # Use the symbols ACGT, '_', and '-', where '_' and '-' represent gaps in the sequence.")
#print("If an invalid symbol is added, you will be asked to start over.")

validChars = set(['A', 'C', 'T', 'G', '-', '_', " "])
seq1 = getValidString(validChars).upper()

print()
print(f"Please enter the second DNA sequence.") #This should be the same length as the first one: {len(seq1)} characters. 

seq2 = getValidString(validChars).upper()

print()
print("Sequences:")
print(seq1)
print(seq2)
print()

print("Please make sure the match input is larger than gap and mismatch, regardless of if the inputs are odd or even.")
match = int(input("Please enter the match reward as an integer: "))
mismatch = int(input("Please enter the mismatch penalty as an integer: "))
gap = int(input("Please enter the gap penalty as an integer: "))

matrix = initialize_matrix(seq1, seq2, match, mismatch, gap)

print("\nThe Needleman-Wunsch Matrix:")
print_matrix(matrix, seq1, seq2)

traceback = findTraceback(matrix)

# fix y axis sequence so that its letters match up with their scores
seq1 = addSpaceToHeader(seq1)

print("\nTraceback chart for the Needleman-Wunsch Matrix:")
print_matrix(traceback, seq1, seq2)