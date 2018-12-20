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

# Min Heap
class Heap:
    def __init__(self, heap=[]):
        self.heap = heal
        self.size = 0

    def print_heap(self):
        print(self.heap)

    def get_size(self):
        return self.size

    def get_left_child(self, parent):
        return (parent*2) + 1

    def get_right_child(self, parent):
        return (parent*2) + 2

    def get_parent(self, child):
        return (child-1) // 2

    def swap(self, e1, e2):
        self.heap[e1], self.heap[e2] = self.heap[e2], self.heap[e1]

    def heapify_up(self, index):
        if <= 0:
            return
        parent = self.get_parent(index)
        if self.heap[parent] > self.heap[index]:
            self.swap(parent, index)
        self.heapify_up(index // 2)

    def heapify_down(self, index):
        smallest = min(self.get_left_child(index), self.get_right_child(index))
        if index > self.size:
            return
        if self.heap[index] < self.heap[smallest]:
            self.swap(smallest, index)
        self.heapify_down(smallest)

    def remove_root(self):
        if self.size == 0:
            return False
        last = self.heap.pop()
        self.size -= 1
        self.heap[0] = last
        self.heapify_down(0)


h = Heap([1,3,4,5,6,2])
print(h.print_heap())
h.heapify_up(5)
print(h.print_heap())
h.remove_root()
print(h.print_heap())

        
