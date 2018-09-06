'''

Heap: A binary tree with two special properties: 
    Shape: A heap must be a complete binary tree in that all levels of the 
        tree must be completely filled - except the last node) 
    Order: A heap's root node must have all its children be less than or 
        equal to or greater than or equal to its children)

    Min Heap: Every single parent node (including the root node) is less 
        than or equal to the value of its children nodes

    Max Heap: Every single parent node (including the root node) is 
        greater than or equal to its children nodes.

Time Complexity: O(n log n)
Space Complexity: O(1)

Implementation:
 insert
 sift_up - needed for insert
 get_max - returns the max item, without removing it
 get_size() - return number of elements stored
 is_empty() - returns true if heap contains no elements
 extract_max - returns the max item, removing it
 sift_down - needed for extract_max
 remove(i) - removes item at index x
 heapify - create a heap from an array of elements, needed for heap_sort
 heap_sort() - take an unsorted array and turn it into a sorted array in-place using a max heap

'''