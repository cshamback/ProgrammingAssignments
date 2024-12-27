import csv

# each algorithm requires two output CSV files 
# one function for each, takes name of file (depends on algorithm and version used) and 2D array of data 
# rows and columns of 2D array correspond to rows and cols of spreadsheet!

def resultsCSV(filename, data):
    with open(filename + '.csv', 'w', newline = '') as file: 
        writer = csv.writer(file)

        # hardcoded header row 
        writer.writerow(["Number One", " Number Two", " Their GCD", " Time Spent (Milliseconds)"])

        # array of data passed as parameter 
        writer.writerows(data[0:])

def statsCSV(filename, data):
    with open(filename + '.csv', 'w', newline = '') as file: 
        writer = csv.writer(file)

        # hardcoded header row 
        writer.writerow(["Statistics", " Milliseconds"])

        # array of data passed as parameter 
        writer.writerows(data[0:])

# add whitespace to items in 2D array so that the data is neatly lined up in the resulting csv file 

def formatData(data):

    # this array is the same length as the number of columns in the 2D array.
    # for each column, it holds the longest string in that column 
    maxLengths = [0] * len(data[0])

    # find the longest string in each column, store in maxLengths
    for i in range(len(data[0])): # iterate through columns in the first row 
        for j in range(len(data)): # for each of those columns, go all the way down through every row 

            if(len(data[j][i]) > maxLengths[i]):
                maxLengths[i] = len(data[j][i])

    # for each item, append maxLengths[col] - data[row][col].length ' ' chars to that item 

    for i in range(len(data[0])): # iterate through columns in the first row 
        for j in range(len(data)): # for each of those columns, go all the way down through every row 

            numSpaces = maxLengths[i] - len(data[j][i])
            data[j][i] = " " + data[j][i] + " " * (numSpaces) # add an extra whitespace at the beginning for readability 
