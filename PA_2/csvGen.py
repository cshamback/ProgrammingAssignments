import csv
import math

#All this does is generate a simple spreadsheet (Formatting is TBD)
def csvGen(fileName, data):
    # Places the csv file in output with an appropriate name.
    with open("PA_2/output/" + fileName + '.csv', 'w') as file:
        # header row/titles 
        fieldnames = ["Input Size ", " Value of n *log(n) ", " Time Spent (Milliseconds) ", " Value of n * log(n) / Time "]

        writer = csv.writer(file) # create writer object 
        writer.writerow(fieldnames) # write a single row for the headers
        writer.writerows(data[0:]) # write the data into more rows 

# ------------------------------------------------------------------------
# STATS ==================================================================
# ------------------------------------------------------------------------

def nLogn(n):
    if(n <= 0):
        print(f"ERROR: n of {n} is invalid for log(n).")
        return 0
    return float(float(n) * math.log(n))

# returns a single row of of the spreadsheet generated for output 
# will be called for each array sorted
# items, in order: input size, nlogn, time spent, nlogn/time
def getStats(arr, timeSpent):

    timeComplexity = nLogn(len(arr))
    timeComplexityScaled = float((timeComplexity) / timeSpent)

    # return the row. all are floats/ints except for timeComplexityScaled, which is a string in scientific notation
    result = [len(arr), timeComplexity, timeSpent, format(timeComplexityScaled, 'e')]
    print(result)
    return result