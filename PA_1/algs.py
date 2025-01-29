# ------------------------------------------------------------------------
# BRUTE FORCE ALGS =======================================================
# ------------------------------------------------------------------------

# start at 1 and try all ints up to the smallest number in the pair 
# since we're looking for the GREATEST common divisor, we have to try all numbers 
def bruteForceV1(pair):
    num1 = pair[0]
    num2 = pair[1]

    gcd = 1

    for i in range(1, min(num1, num2)):
        if((num1 / i).is_integer() and (num2 / i).is_integer()):
            gcd = i

    return gcd

# start at the smaller number in the pair and work backwards to 1
# since we're looking for the GREATEST common divisor, we can stop when we find one 
def bruteForceV2(pair):
    num1 = pair[0]
    num2 = pair[1]

    start = min(num1, num2)
    gcd = start 

    for i in range(start, 1, -1):
        if((num1 / i).is_integer() and (num2 / i).is_integer()):
            return i 

    return 1

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
            # it is possible that b (the smaller number) IS the GCD
            # in that case, return it 
            if (b * q) == a: 
                return b 
            else: 
                return r 
        else:
            r = tempR

        # assign new a and b 
        a = b
        b = r

    return prevR

# second Euclidean algorithm 
def euclidV2(pair):
    #inputs
    a = 0
    b = 0
    num1 = pair[0]
    num2 = pair[1]
    #none because it is an absent value
    remainder = None

    # ensures proper placement before the while operation begins. 
    if num1 > num2:
        a = num1
        b = num2
    else:
        a = num2
        b = num1

    while(remainder != 0):
        remainder = a - b
        if(remainder >= b):  #meaning quotient > 1
            remainder = remainder - b 
            if(remainder >= b): #meaning quotient > 2
                remainder = remainder - b
                if(remainder >= b): #meaning quotient > 3
                    # floor division operation
                    q = a // b
                    remainder = a - (b * q)
        # reassign values for the next cycle in the while loop
        a = b
        b = remainder

    return a