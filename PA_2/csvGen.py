import csv
import math

#Everything is WIP. So everything is a demo and subject to change.
#All this does is generate a simple spreadsheet (Formatting is TBD)
def csvGen(fileName, data):
    # Places the csv file in output with an appropriate name.
    with open("PA_2/output/" + fileName + '.csv', 'w') as file:
        #This part of code deals with headers
        fieldnames = ["Input Size ", " Value of n *log(n) ", " Time Spent (Milliseconds) ", " Value of n * log(n) / Time "]
        heading = csv.DictWriter(file,fieldnames= fieldnames ,delimiter= ',')
        heading.writeheader()
        #The gap in this matters
        csvWriter = csv.writer(file, delimiter= ',')
        csvWriter.writerow(data[0:]) 


#Test spreadsheet making
csvGen("Testing",[1,2,3,4])

# ------------------------------------------------------------------------
# STATS ==================================================================
# ------------------------------------------------------------------------

def nLogn(n):
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

# ------------------------------------------------------------------------
# STATS ==================================================================
# ------------------------------------------------------------------------

def nLogn(n):
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