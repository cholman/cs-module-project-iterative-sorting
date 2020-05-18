def linear_search(arr, target):
        # Your code here
    i = 0
    while i < len(arr):
        if arr[i] == target:
            return i
        i += 1

    return -1 # not found


# Write an iterative implementation of Binary Search
def binary_search(arr, target):

    # Your code here
    #set lower to index 0
    lower = 0
    upper = len(arr)-1
    
    #while lower is less than or = to upper:
    while lower <= upper:
        #set mid to lower + upper / 2
        mid = (lower + upper) // 2
        #if the middle point = our target, return it
        if arr[mid] == target:
            return mid
        else:
            #otherwise if it is less than target, set lower to mid
            if arr[mid] < target:
                lower = mid
            else:
                upper = mid


    return -1  # not found
