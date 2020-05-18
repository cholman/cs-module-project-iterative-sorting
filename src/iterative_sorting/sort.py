def selection_sort(arr):
    for i in range(0, len(arr)):
        #for each index, set current_index to i
        current_index = i
        print(arr, "i")
        for j in range(i, len(arr)):
            # compare current index against all other indices
            if arr[j] < arr[current_index]:
                # if compared index is less than current_index
                current_index = j
                # set current_index to new index, then swap them
                print(arr, "j")

        #swap i and current_index
        temp = arr[i]
        arr[i] = arr[current_index]
        arr[current_index] = temp
        #return to top of i loop, resetting current_index




nums = [4, 6, 8, 5, 3, 2, 7]
#selection_sort(nums)

def bubble_sort(arr):
    #for each index, going backwards from last to first
    for i in range(len(arr)-1, 0, -1):
        for j in range(i):
            if arr[j] > arr[j+1]:
                #swap
                temp = arr[j]
                arr[j] = arr[j+1]
                arr[j+1] = temp

bubble_sort(nums)
print(nums)