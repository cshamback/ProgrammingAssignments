# This file is to just test out code or ideas. When done, please revert it back to how it was.

#---------------------------------------------------------------------
#Start Below =========================================================
#---------------------------------------------------------------------
from csvGen import * 
from mergeSort import * 
#Testing how this would work. Now we just need for it to do this 9 more times. - LC
bigArray = []
for instance in range (9):
    subArray = []
    subArray.append(f"Array_{instance}")
    for i in range(4):
        subArray.append(randomNumberFill(1,99))
    
    
    print(subArray)
    bigArray.append(subArray)

print("Testing Data [All together]:", bigArray)
# Test
# Steve was here
print(bigArray[1][1])