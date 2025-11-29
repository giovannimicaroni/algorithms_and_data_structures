def binary_search(array, target):
    '''
    Given a sorted array, finds the target value in O(log n).
    If the target is in the array, returns it index. Otherwise, returns None.
    '''
    lower = 0
    higher = len(array)-1
    while lower <= higher:
        middle = (lower + higher)//2
        value = array[middle]
        if value == target:
            return middle
        elif value < target:
            lower = middle + 1
        else:
            higher = middle - 1
    
    return None

if __name__ == "__main__":
    array = list(range(1, 101))
    print(binary_search(sorted(array), 42)) 
