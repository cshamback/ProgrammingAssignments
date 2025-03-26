# MAIN
from utils import *

print("* * * * * * * * * * * * * * * * * * * * * * * * * * * * * * *")
print("* P A 6  N E E D L E M A N - W U N S C H  A L G O R I T H M *")
print("* * * * * * * * * * * * * * * * * * * * * * * * * * * * * * *")
print()

print("Please enter the first DNA sequence. Use the symbols ACGT, '_', and '-', where '_' and '-' represent gaps in the sequence.")
print("If an invalid symbol is added, you will be asked to start over.")

validChars = set(['A', 'C', 'T', 'G', '-', '_'])
seq1 = getValidString(validChars).upper()

print()

print(f"Please enter the second DNA sequence. This should be the same length as the first one: {len(seq1)} characters.")
print(f"If it is too short, a string of the '-' character will be appended to it. If it is too long, it will be truncated.")

seq2 = getValidString(validChars).upper()

print()

# adjust seq2 if they are not the same length
if(len(seq2) > len(seq1)):
    seq2 = seq2[0 : len(seq1)]
if(len(seq2) < len(seq1)):
    seq2 = seq2 + ("-" * (len(seq1) - len(seq2)))

print("Sequences, adjusted for length: ")
print(seq1)
print(seq2)
print()

match = int(input("Please enter the match reward as an integer: "))
mismatch = int(input("Please enter the mismatch penalty as an integer: "))
gap = int(input("Please enter the gap penalty as an integer: "))