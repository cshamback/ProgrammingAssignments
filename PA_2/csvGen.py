import csv
import math

#All this does is generate a simple spreadsheet (Formatting is TBD)
def csvGen(fileName, data):
    # Places the csv file in output with an appropriate name.
    with open("PA_2/output/" + fileName + '.csv', 'w', newline=' ') as file: 
        # header row/titles 
        fieldnames = ["Input Size ", " Value of n *log(n) ", " Time Spent (Milliseconds) ", " Value of n * log(n) / Time "]

        writer = csv.writer(file) # create writer object 
        writer.writerow(fieldnames) # write a single row for the headers

        # Ensures proper number formatting in rows
        formatted_data = [[f"{x}", f"{y:.6f}", f"{z:.6f}", f"{w:.6e}"] for x, y, z, w in data]
        writer.writerows(formatted_data) # write the data into more rows and keeps it formatted

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

    # Just makes sure we don't divide by zero
    if timeSpent == 0:
        timeComplexityScaled = 0
    else:
        timeComplexityScaled = float((timeComplexity) / timeSpent)

    # return the row. all are floats/ints except for timeComplexityScaled, which is a string in scientific notation
    result = [len(arr), timeComplexity, timeSpent, format(timeComplexityScaled, 'e')]
    print(result)
    return result