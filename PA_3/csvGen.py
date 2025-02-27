import csv
from Fibonacci import*
import math
def generateCsv(filename, data):
    #output file location and name
    output_to = "PA_3/output/" + filename + '.csv'

    with open(output_to, 'w', newline='') as FibFile:
        csv_writer = csv.writer(FibFile)

        #Field names specified in PA-3 sheet
        fieldNames = ['n', 'F(n)', 'T1: Time spent on recursive algorithm', 'T2: Time spent on dynamic algorithm', 'Value of (2^n)/n', 'Value of T1/T2']
        #Write these field names into spreadsheet
        csv_writer.writerow(fieldNames)

        formats = [
            [f"{int(a)}", f"{int(b)}", f"{c:.10f}", f"{d:.10f}", f"{e:.10e}", f"{f:.10e}"]
            for a,b,c,d,e,f in data
        ]
        csv_writer.writerows(formats)


# All statistics would be formatted and returned in a way that other functions can take the final result as an input
# to write to spreadsheet
def statistics(n,Fn,Recursive, Dynamic, ScaledItems, AggregateTime):
    finalResult = [n, Fn, Recursive, Dynamic, ScaledItems, AggregateTime]
    #print(finalResult)
    return finalResult