#  </> Algorithms and Data Structures

### Python implementation of common algorithms and data structures.

This repository is a collection of fundamental algorithms and data structures implemented in Python. It was built as a learning resource, a quick reference, and a place to practice core computer science concepts.

## 🏗️ Data Structures Implemented

This section lists the data structures currently available in the repository.

| Structure | Description | Access | Insertion | Deletion |
| :--- | :--- | :---: | :---: | :---: |
| [**Singly Linked List**](data_structures/linked_list.py) | A linear collection of data elements pointing to the next node. This implementation has head and tail pointers. | `O(n)` | `O(1)` | `O(1)` |
| [**Array**](data_structures/array.py) | Contiguous memory blocks allowing instant access by index. | `O(1)` | `O(n)` | `O(n)` |
| [**Stack**](data_structures/stack.py) | LIFO (Last-In, First-Out) collection. Elements are added/removed from the "top". | `O(n)` | `O(1)` | `O(1)` |


## 🧠 Algorithms Implemented

This section details the various algorithmic categories and examples available.

### Sorting Algorithms
| Algorithm | Description | Time complexity |
| :--- | :--- | :--- |
| [Binary Search](algorithms/binary_search.py) | Given a sorted array and a target value, if the target is in the array, returns the index of the target. Otherwise, returns None | `O(log n)` |
| [Selection Sort](algorithms/selection_sort.py) | Given an array of integers, returns the sorted version of this array. | `O(n²)` |
| [QuickSort](algorithms/quicksort.py) | Given an array of integers, returns the sorted version of this array. | `O(n*log n)` |
