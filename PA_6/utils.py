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