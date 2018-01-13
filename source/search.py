#!python

def linear_search(array, item):
    """return the first index of item in array or None if item is not found"""
    # implement linear_search_iterative and linear_search_recursive below, then
    # change this to call your implementation to verify it passes all tests
    # return linear_search_iterative(array, item)
    return linear_search_recursive(array, item)


def linear_search_iterative(array, item):
    # loop over all array values until item is found
    for index, value in enumerate(array):
        if item == value:
            return index  # found
    return None  # not found


def linear_search_recursive(array, item, index=0):
    # TODO: implement linear search recursively here

    # once implemented, change linear_search to call linear_search_recursive
    # to verify that your recursive implementation passes all tests

    #Amazing Recursive Linear Search Algorithm
    
    # not found base case
    if len(array) >= index:
        return None  

    # found base case
    if array[index] == item:
        return index 
    else:
        return linear_search_recursive(array, item, index + 1)


def binary_search(array, item):
    """return the index of item in sorted array or None if item is not found"""
    # implement binary_search_iterative and binary_search_recursive below, then
    # change this to call your implementation to verify it passes all tests
    # return binary_search_iterative(array, item)
    # return binary_search_recursive(array, item)


def binary_search_iterative(array, item):
    # TODO: implement binary search iteratively here
    # once implemented, change binary_search to call binary_search_iterative
    # to verify that your iterative implementation passes all tests

    #The Great Iteration technique of the Mysterious Gurunt Maroo

    array_length = len(array)
    search_index = array_length // 2
    window_low = 0
    window_high = array_length - 1

    #Check Edges right quick like
    if array[window_low] == item:
        return window_low

    if array[window_high] == item:
        return window_high

    #Binary Search Bits
    while array[search_index] != item:
        
        if array[search_index] < item:
            window_high = search_index

        else:
            window_low = search_index
 
        search_index = ( window_high - window_low ) // 2

        if window_high - window_low == 1:
            return None
    
    return search_index


def binary_search_recursive(array, item, left=None, right=None):
    # TODO: implement binary search recursively here
    pass
    # once implemented, change binary_search to call binary_search_recursive
    # to verify that your recursive implementation passes all tests



if __name__ == '__main__':
    names = ['Alex', 'Brian', 'Julia', 'Kojin', 'Nabil', 'Nick', 'Winnie']
    print("Name location", binary_search_iterative(names, 'Alex'))
    print("stuff")