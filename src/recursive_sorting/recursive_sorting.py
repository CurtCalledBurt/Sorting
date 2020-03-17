test_arr = [2, 1, 3, 5, 2, 4]
test_arr2 = [9, 6, 3, 4, 5, 6, 7, 8, 3, 4, 2, 4, 3, 4]

def partition(arr, low, high):
    index_small = low - 1           # index of smaller element, this is -1 to start
    pivot = arr[high]               # pivot

    for i in range(low, high):
        # excecute if current element is smaller than pivot
        if arr[i] < pivot:
            # makes index_small 0, then 1, then 2, etc each an elem to the left of pivot is found
            index_small += 1
            # switches the positions of the current elem smaller than the pivot with
            # whatever is in the place on the left of the array we are putting it in
            arr[index_small], arr[i] = arr[i], arr[index_small]

    arr[index_small+1], arr[high] = arr[high], arr[index_small+1]
    return arr, index_small + 1

def quicksort(arr, low, high):
    if low < high:
        _, partition_index = partition(arr, low, high)
        quicksort(arr, low, partition_index - 1)
        quicksort(arr, partition_index + 1, high)
    return arr

array = test_arr
print(quicksort(array, 0, len(array) - 1))


# TO-DO: complete the help function below to merge 2 sorted arrays
def merge( arrA, arrB ):
    elements = len( arrA ) + len( arrB )
    merged_arr = [0] * elements
    i = j = k = 0
    # merges elements in left and right arrays until one array is depleted
    while i < len(arrA) and j < len(arrB):
        if arrA[i] < arrB[j]:
            merged_arr[k] = arrA[i]
            i += 1
        else:
            merged_arr[k] = arrB[j]
            j += 1
        k += 1
    # finishes adding any elements to the merged array from the undepleted array
    while i < len(arrA):
        merged_arr[k] = arrA[i]
        i += 1
        k += 1
    while j < len(arrB):
        merged_arr[k] = arrB[j]
        j += 1
        k += 1
    return merged_arr

def merge_sort( arr ):
    # base case is len(arr) < 2
    if len(arr) > 1:
        # get middle index
        mid_index = len(arr) // 2
        # divide array into two halves
        # in this case, by how python does splicing the pivot is in the right array
        left_arr = arr[:mid_index]
        right_arr = arr[mid_index:]

        # recurse the function on the two split arrays and sort them individually
        left_arr = merge_sort(left_arr)
        right_arr = merge_sort(right_arr)

        # merge and sort the two sorted arrays together
        arr = merge(left_arr, 
                    right_arr)

    return arr

# print(merge_sort(test_arr))


# STRETCH: implement an in-place merge sort algorithm
def merge_in_place(arr, start, mid, end):
    # TO-DO

    return arr

def merge_sort_in_place(arr, l, r): 
    # TO-DO

    return arr


# STRETCH: implement the Timsort function below
# hint: check out https://github.com/python/cpython/blob/master/Objects/listsort.txt
def timsort( arr ):

    return arr
