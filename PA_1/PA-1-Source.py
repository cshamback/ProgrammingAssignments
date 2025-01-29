# Brute Force and Euclid's GCD Algorithms

from csvGen import *
from algs import *

import random
from datetime import datetime

# generate 1000 pairs of random integers
pairs = [[0] * 2 for _ in range(1000)]  # 1000 rows and 2 cols

for i in range(len(pairs)):
    for j in range(len(pairs[i])):
        pairs[i][j] = random.randint(1, 1000)

# --------------------------------------------------------
# BRUTE FORCE ALGS =======================================
# --------------------------------------------------------

# each table gets its own 2D array. Each of these will be generated as a separate CSV file. 
bfResultsV1 = [[] * 4] * 1000 # results: num1, num2, GCD, time elapsed 
bfResultsV2 = [[] * 4] * 1000

bfStatsV1 = [[] * 2] * 1000
bfStatsV2 = [[] * 2] * 1000

# run v1
print("brute force v1...")
for i in range(0, len(pairs)): # iterate through rows 
    currentTime = datetime.now()
    gcd = bruteForceV1(pairs[i])
    newTime = datetime.now()

    bfResultsV1[i] = [str(pairs[i][0]), str(pairs[i][1]), str(gcd), str((newTime - currentTime).total_seconds() * 1000)]

# run v2
print("brute force v2...")
for i in range(0, len(pairs)): # iterate through rows 
    currentTime = datetime.now()
    gcd = bruteForceV2(pairs[i])
    newTime = datetime.now()

    bfResultsV2[i] = [str(pairs[i][0]), str(pairs[i][1]), str(gcd), str((newTime - currentTime).total_seconds() * 1000)]

# generate results spreadsheet for v1 and v2

print("formatting data and getting results...")

formatData(bfResultsV1, ["Number One", "Number Two", "Their GCD", "Time Spent (Milliseconds)"])
formatData(bfResultsV2, ["Number One", "Number Two", "Their GCD", "Time Spent (Milliseconds)"])

csvGen("BF_v1_Results", bfResultsV1, ["Number One", " Number Two", " Their GCD", " Time Spent (Milliseconds)"])
csvGen("BF_v2_Results", bfResultsV2, ["Number One", " Number Two", " Their GCD", " Time Spent (Milliseconds)"])

# generate statistics spreadsheet for v1 and v2

# returns 2D array with max/min/average/median
bfStatsV1 = getStats(bfResultsV1)
bfStatsV2 = getStats(bfResultsV2)

# formats that data 
formatData(bfStatsV1, ["Statistics", "Milliseconds"])
formatData(bfStatsV2, ["Statistics", "Milliseconds"])

# generates csv 
csvGen("BF_v1_Statistics", bfStatsV1, ["Statistics", " Milliseconds"])
csvGen("BF_v2_Statistics", bfStatsV2, ["Statistics ", " Milliseconds"])

print("brute force done!")

# --------------------------------------------------------
# EUCLIDEAN ALGS =========================================
# --------------------------------------------------------

# each table gets its own 2D array. Each of these will be generated as a separate CSV file. 
oeResults = [[] * 4] * 1000
seResults = [[] * 4] * 1000

oeStats = [[] * 2] * 1000
seStats = [[] * 2] * 1000

# run euclid v1

print("euclid v1...")
for i in range(0, len(pairs)): # iterate through rows 
    currentTime = datetime.now()
    gcd = euclidV1(pairs[i])
    newTime = datetime.now()

    oeResults[i] = [str(pairs[i][0]), str(pairs[i][1]), str(gcd), str((newTime - currentTime).total_seconds() * 1000)]

# run euclid v2
print("euclid v2...")
for i in range(0, len(pairs)): # iterate through rows 
    currentTime = datetime.now()
    gcd = euclidV2(pairs[i])
    newTime = datetime.now()

    seResults[i] = [str(pairs[i][0]), str(pairs[i][1]), str(gcd), str((newTime - currentTime).total_seconds() * 1000)]
# generate results spreadsheet for v1 and v2

print("formatting data and getting results...")
formatData(oeResults, ["Number One", "Number Two", "Their GCD", "Time Spent (Milliseconds)"])
formatData(seResults, ["Number One", "Number Two", "Their GCD", "Time Spent (Milliseconds)"])

csvGen("OE_Results", oeResults, ["Number One", "Number Two", "Their GCD", "Time Spent (Milliseconds)"])
csvGen("SE_Results", seResults, ["Number One", "Number Two", "Their GCD", "Time Spent (Milliseconds)"])

# generate statistics spreadsheet for v1 and v2

# returns 2D array with max/min/average/median
oeStats = getStats(oeResults)
seStats = getStats(seResults)

# formats that data 
formatData(oeStats, ["Statistics", "Milliseconds"])
formatData(seResults, ["Statistics", "Milliseconds"])

# generates csv 
csvGen("OE_Statistics", oeStats, ["Statistics", " Milliseconds"])
csvGen("SE_Statistics", seStats, ["Statistics", " Milliseconds"])

print("euclid done!")

# --------------------------------------------------------
# CONCLUSIONS.TXT ========================================
# --------------------------------------------------------