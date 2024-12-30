# ------------------------------------------------------------------------
# BRUTE FORCE ALGS =======================================================
# ------------------------------------------------------------------------

# start at 1 and try all ints up to the smallest number in the pair 
def bruteForceV1(pair):
    num1 = pair[0]
    num2 = pair[1]

    gcd = 1

    for i in range(1, min(num1, num2)):
        if((num1 / i).is_integer() and (num2 / i).is_integer()):
            gcd = i

    return gcd

# start at the smaller number in the pair and work backwards to 1
def bruteForceV2(pair):
    num1 = pair[0]
    num2 = pair[1]

    start = min(num1, num2)
    gcd = start 

    for i in range(start, 1, -1):
        if((num1 / i).is_integer() and (num2 / i).is_integer()):
            gcd = i

    return gcd

# ------------------------------------------------------------------------
# EUCLIDEAN ALGS =========================================================
# ------------------------------------------------------------------------

# formula: a = bq + r

# base Euclidean algorithm 
def euclidV1(pair):
    num1 = pair[0]
    num2 = pair[1]

    a = 0 # the larger of num1, num2
    b = 0 # the smaller of num1, num2
    q = 0 # quotient
    r = None # remainder 

    prevR = None # remainder from prev. step => updated every step; returned when r = 0 

    if num1 > num2: 
        a = num1
        b = num2
    else: 
        a = num2
        b = num1

    while(r != 0):
        
        # assign q and r 
        q = a // b # // is the floor division operator
        tempR = a - (b * q)
        
        # if the new remainder is 0, we've gone too far. 
        # return the previous r value, and we're done 
        if tempR == 0: 
            return r 
        else:
            r = tempR

        # assign new a and b 
        a = b
        b = r

    return prevR

# second Euclidean algorithm 
# def euclidV2(pair):