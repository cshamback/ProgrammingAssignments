import csv
import math

#All this does is generate a simple spreadsheet (Formatting is TBD)
def csvGen(fileName, data):
    output_file = "PA_2/output/" + fileName + '.csv'

    with open(output_file, 'w', newline='') as file:
        writer = csv.writer(file)

        # Write headers with uniform spacing
        fieldnames = ["Input Size", "Value of n * log(n)", "Time Spent (Milliseconds)", "Value of n * log(n) / Time"]
        writer.writerow(fieldnames)

        # Format each row properly with spacing
        formatted_data = [
            [f"{x:<10}", f"{y:<20.6f}", f"{z:<20.6f}", f"{w:<20.6e}"]
            for x, y, z, w in data
        ]
        writer.writerows(formatted_data)

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

    if timeSpent == 0:
        timeComplexityScaled = 0
    else:
        timeComplexityScaled = float((timeComplexity) / timeSpent)

    # return the row. all are floats/ints except for timeComplexityScaled, which is a string in scientific notation
    result = [len(arr), timeComplexity, timeSpent, timeComplexityScaled]
    print(result)
    return result