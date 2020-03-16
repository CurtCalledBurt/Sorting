test_arr = [10, 9, 8, 7, 3, 4, 5, 2, 6, 1]

# TO-DO: Complete the selection_sort() function below 
def selection_sort( arr ):
    print("\n Selection Sort")
    # loop through n-1 elements
    for i in range(0, len(arr) - 1):
        cur_index = i
        smallest_index = cur_index
        # TO-DO: find next smallest element
        # (hint, can do in 3 loc)
        for j in range(cur_index + 1, len(arr)):
            # find the index of the smallest unsorted element
            if arr[j] < arr[smallest_index]:
                smallest_index = j
        # perform the swap in memory
        temp = arr[cur_index]
        arr[cur_index] = arr[smallest_index]
        arr[smallest_index] = temp
        # print the array for debugging purposes
        print(arr)
    return arr

selection_sort(test_arr)

# TO-DO:  implement the Bubble Sort function below

""" 
As a note, I've always thought that bubble sort really ought be called sink sort, or rock sort or something like that. Becuase it's less like the entrees float to the top, and more like the really heavy objects sink.
"""
def bubble_sort( arr ):
    print("\n\n Bubble Sort")
    for i in range(len(arr)):
        # for bubble sort we need to run through the entire list len(list) # of times
        # so j always starts at 0
        j = 0
        temp = arr[j]
        while j < len(arr) - i - 1:
            # if the previous position is bigger than the next, switch them
            if temp > arr[j+1]:
                arr[j] = arr[j+1]
                arr[j+1] = temp
            # after a switch or non-switch, the bigger number will always be in the j+1 postion
            # so we switch temp to the next position
            temp = arr[j+1]
            # increase j to end the while loop as efficiently as possible
            j += 1
        # print the array after one full runthrough of the array of switches to check it is sorting correctly.
        print(arr)
    return arr

bubble_sort(test_arr)

test_count_array = [7, 3, 5, 6, 3, 2, 1, 2, 4, 5, 3, 2, 3, 1, 2, 3, 1, 9, 5, 2, 1, 3]

# STRETCH: implement the Count Sort function below
def count_sort( arr, maximum=-1 ):
    print("\n\n Count Sort")
    # 1) creation of the count array
    # find maximum of the array
    for elem in arr:
        if elem > maximum:
            maximum = elem
    # create count array
    count_array = [0] * (maximum + 1)

    # 2) do the counting
    for i in range(len(arr)):
        count_array[arr[i]] += 1
    print( f" {count_array}")

    # 3) find the new indexes
    sum = 0
    sum_array = [0] * (maximum + 1)
    for i in range(len(count_array)):
        sum += count_array[i]
        sum_array[i] = sum
    print("\n", sum_array)

    # 4) put everything where it belongs
    
    return arr

count_sort(test_count_array)