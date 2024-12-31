# merges 2 subarrays, arr1 and arr2 (used in mergeSort() below)

# l and r are the beginning and ending indices of the merge region
# arr1 and arr2 are the sorted left and right arrays that belong inside that region 
def merge(arr1, arr2):
    result = []

    i = 0 # tracks arr1
    k = 0 # tracks arr2

    # iterate through arr1 and arr2 at the same time
    # one at a time, pick the smaller of the two items currently being looked at
    # append that item to the result array 
    while(i < len(arr1) or k < len(arr2)):

        # important: Append adds a single element to the end of a list.
        # extend ends multiple elements.

        # handle running out of elements in arr1 or arr2
        if(i >= len(arr1)): 
            result.extend(arr2[k:]) # run out of arr1 elements, append the rest of arr2 elements 

            # return, do not append any more elements 
            return result

        if(k >= len(arr2)):
            result.extend(arr1[i:]) # run out of arr2 elements, append the rest of arr1 elements 

            # return, do not append any more elements 
            return result
        
        # if there are still elements in both arr1 and arr2, 
        # decide which one is smaller and append it 
        if(arr1[i] < arr2[k]): 
            result.append(arr1[i])
            i = i + 1
        else:
            result.append(arr2[k])
            k = k + 1

    return result

# merge portion of array - overload 
# l and r are start and end points of subarrays inside data 
def mergeSort(l, r, data): 

    # not really a base case, just prevent us from walking off the end of the array
    if(l < len(data)):

        # BASE CASE 
        # if there is only one element left in the subarray, return a deep copy of it 
        if(l == r): 
            return [data[l]] 
        
        # divide remaining data 
        mid = (l + r) // 2

        # both of these recurse until all subarrays are split into single elements 
        left = mergeSort(l, mid, data) # merge sort left subarray -> [left, mid]
        right = mergeSort(mid + 1, r, data) # merge sort right subarray -> [mid + 1, right]

        # recurses from single elements to complete list 
        return merge(left, right) # merge left and right subarrays 
    else:
        return []