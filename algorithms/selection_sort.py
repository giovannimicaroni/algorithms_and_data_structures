def find_lowest(array):
    '''
    Given an array of integers, returns the index of the lowest value.
    '''
    if array is None or len(array) == 0:
        return None
    lowest = array[0]
    lowest_index = 0
    for i in range(1, len(array)):
        if array[i] < lowest:
            lowest = array[i]
            lowest_index = i

    return lowest_index

def selection_sort(array):
    ''''
    Takes an array of integers as parameter and sorts it in O(n²). Returns the sorted array.
    '''
    sorted_array = []
    for i in range(len(array)):
        lowest_index = find_lowest(array)
        sorted_array.append(array.pop(lowest_index))
    return sorted_array

if __name__ == "__main__":
    array = [3, 7, 2, 1, 9, 11]
    print(selection_sort(array))
