

def linear_search(array, item):
    """return the first index of item in array or None if item is not found"""
    # implement linear_search_iterative and linear_search_recursive below, then
    # change this to call your implementation to verify it passes all tests
    return linear_search_recursive(array, item)
    # return linear_search_recursive(array, item)


def linear_search_iterative(array, item):
    # loop over all array values until item is found
    for index, value in enumerate(array):
        if item == value:
            return index  # found
    return None  # not found


def linear_search_recursive(array, item, index=0):
    if array:
        if array[0] == item: # base case - first index is key
            return index
        s = linear_search_recursive(array[1:], item, index+1) # recursion        
        if s is not False:
            print('here found s:', s)
            return s

    
    return None # returns false if key not found

def binary_search(array, item):
    """return the index of item in sorted array or None if item is not found"""
    # implement binary_search_iterative and binary_search_recursive below, then
    # change this to call your implementation to verify it passes all tests
    return binary_search_recursive(array, item)
    # return binary_search_recursive(array, item)


def binary_search_iterative(array, item):
    left = 0
    right = len(array) # O(n)
    while True: 
        if left >= right: # edge case
            return -1
        mid = right - left // 2
        if mid == item: # base base
            return mid 
        else:
            if array[mid] < item:
                right = mid - 1
            else: # array[mid] > item
                left = mid + 1
    
    # return False # or raise error


def binary_search_recursive(array, item):
    print('array:', array)
    if len(array) == 0:
        return None
    mid_index = len(array) // 2
    mid = array[mid_index]
    print('mix_index:', mid_index)
    print('middle item:', mid)
    if mid == item: # Base Case
        print('mid == item!')
        return mid_index
    if mid < item:
        print('mid < item :(')
        return binary_search_recursive(array[mid_index+1:], item)
    print('mid > item :(') # mid > item
    return binary_search_recursive(array[:mid_index], item)