<<<<<<< HEAD
'''

Insertion Sort: An in-place comparison-based sorting algorithm. Here, a 
    sub-list is maintained which is always sorted. The array is searched
    sequentially and unsorted items are moved and inserted into the sorted 
    sub-list (in the same array). Not suitable for large data sets.


Time Compmlexity (Best): O(n)
Time Complexity (Average and Worst): O(n^2)
Space Complexity: O(1)

Implementation:
Insertion Sort

'''

def insertion_sort(alist):
    for i in range(1, len(alist)):
        key = alist[i]
        j = i - 1 # Sorted array index

        # Finding a spot for key in sorted array
        while j >= 0 and key < alist[j]:
            alist[j+1] = alist[j]
            j -= 1
        
        # If j is less than key, insert key into j+1 position
        alist[j+1] = key
        
    return alist

def main():
    arr = [7,1,5,2,4,3,6,9,8]
    print(insertion_sort(arr))

if __name__ == "__main__":
    main()
=======
def insertionSort(alist):
    for x in range(1,len(alist)-1):
        value = alist[x]
        sorted_position = x - 1

        while sorted_position >= 0 and alist[sorted_position] > value:
            alist[sorted_position+1] = alist[sorted_position]
            sorted_position -= 1

        alist[sorted_position+1] = value
    return alist

def main():
    arr = [6,1,4,2,7,8,9]
    print(insertionSort(arr))

if __name__ == '__main__':
    main() 
>>>>>>> ebc70956cdd07d48336152a3fb3fb54a7e048efd
