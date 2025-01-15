import csv

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