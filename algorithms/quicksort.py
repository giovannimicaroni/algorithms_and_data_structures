import random

def quicksort(array):
    """Sort array using quicksort with random pivot selection."""
    if len(array) < 2:
        return array
    else:
        pivot_index = random.randint(0, len(array) - 1)
        pivot = array[pivot_index]

        lower = [x for x in array if x < pivot]
        equal = [x for x in array if x == pivot]
        higher = [x for x in array if x > pivot]

        return quicksort(lower) + equal + quicksort(higher)
    
if __name__ == "__main__":
    print(quicksort([3, 1, 2, 7, 2, 10, 9]))
