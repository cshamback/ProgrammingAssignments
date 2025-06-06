import csv
from Fibonacci import*
import math
def generateCsv(filename, data):
    #output file location and name
    output_to = "PA_3/output/" + filename + '.csv'

    with open(output_to, 'w', newline='') as FibFile:
        csv_writer = csv.writer(FibFile)

        #Field names specified in PA-3 sheet
        fieldNames = ['n', 'F(n)', 'T1: Time spent on recursive algorithm (Seconds)', 'T2: Time spent on dynamic algorithm (Seconds)', 'Value of (2^n)/n', 'Value of T1/T2 (Seconds)']
        #Write these field names into spreadsheet
        csv_writer.writerow(fieldNames)

        formats = [
            [
             f"{int(a):>1}",
             f"{int(b):>10}", 
             f"{c:>20.10f}", 
             f"{d:>20.10f}", 
             f"{e:>20.5e}", 
             f"{f:>20.5e}"
             ]
            for a,b,c,d,e,f in data
        ]
        csv_writer.writerows(formats)


# All statistics would be formatted and returned in a way that other functions can take the final result as an input
# to write to spreadsheet
def statistics(n,Fn,Recursive, Dynamic, ScaledItems, AggregateTime):
    finalResult = [n, Fn, Recursive, Dynamic, ScaledItems, AggregateTime]
    #print(finalResult)
    return finalResult