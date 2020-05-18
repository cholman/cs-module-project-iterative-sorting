def linear_search(arr, target):
     # Your code here
    i = 0
    while i < len(arr):
        if arr[i] == target:
            return i
        i += 1

    return -1  # not found

nums = [5, 8, 4, 6, 9, 2]

#print(linear_search(nums, 2))

def binary_search(arr, target):

    lower = 0
    upper = len(arr)-1
    
    while lower <= upper:
        mid = (lower + upper) // 2

        if arr[mid] == target:
            globals()['pos'] = mid
            return mid
        else:
            if arr[mid] < target:
                lower = mid
            else:
                upper = mid




print(binary_search(nums, 9))