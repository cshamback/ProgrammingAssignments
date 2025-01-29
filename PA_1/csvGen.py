import csv

# each algorithm requires two output CSV files 
# one function for each, takes name of file (depends on algorithm and version used) and 2D array of data 
# rows and columns of 2D array correspond to rows and cols of spreadsheet!

def csvGen(filename, data, headerRow):
    with open("PA_1/output/" + filename + '.csv', 'w', newline = '') as file: 
        writer = csv.writer(file)

        # header row is passed as a param, so it doesn't have to be part of the data array
        writer.writerow(headerRow)

        # array of data passed as parameter 
        writer.writerows(data[0:])

# add whitespace to items in 2D array so that the data is neatly lined up in the resulting csv file 

def formatData(data, headingRow):

    # this array is the same length as the number of columns in the 2D array.
    # for each column, it holds the longest string in that column 
    maxLengths = [0] * len(headingRow[0])

    # first, set the max lengths to the lengths of the header strings
    # these are not part of the data array, so use them as the starting point
    for i in range(len(headingRow)):
        maxLengths[i] = len(headingRow[i])

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

# find minimum, maximum, average, and median for statistics csvs 
# data is a 1D array representing the last column (time) of the results csv.

def getStats(data):
    data.sort()
    median = data[len(data) // 2][3] # floor division to find the "middle" of the array

    total = 0.0
    maxTime = 0
    minTime = float('inf') # represents positive infinity as a float 

    # iterate through each row in the 2D array
    # always look at the last column (index 3)
    for i in range(0, len(data)):
        total = total + float(data[i][3])

        if float(data[i][3]) > float(maxTime): 
            maxTime = data[i][3]
        if float(data[i][3]) < float(minTime): 
            minTime = data[i][3]

    avg = float(total) / 1000 # hard coded, fine for the purposes of this assignment since they never require any number other than 1000 

    # leave as string for storage - need to use string function len() when formatting table 
    return [
        ["Maximum Time", str(maxTime)],
        ["Minumum Time", str(minTime)],
        ["Average Time", str(avg)],
        ["Median Time", str(median)]
    ]
