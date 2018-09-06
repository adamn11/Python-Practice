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
insert (O(1))
remove (O(n log n))
heapify_up
heapify_down
get_max
get_size

'''