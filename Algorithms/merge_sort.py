'''

Merge Sort: Sort an array, divide it into two halves, sort the two halves (recursively), 
    and then merge the results.

Time Complexity:  O(n log n)
Space Complexity: O(n)

Implementation:
Top-Down
Bottom-Up

'''

# Top-down Implementation
def merge_sort_top_down(alist):
    if len(alist) > 1:
        mid = len(alist) // 2
        left = alist[:mid]
        right = alist[mid:]

        merge_sort_top_down(left)
        merge_sort_top_down(right)

        i = 0 # Index for left alist
        j = 0 # Index for right alist
        k = 0 # Index for original alist

        # Comparing left and right alist and inserting the smallest one into original alist
        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                alist[k] = left[i]
                i += 1
            else:
                alist[k] = right[j]
                j += 1
            k += 1
        
        # Inserting elements from left alist when elements from right alist are empty
        while i < len(left):
            alist[k] = left[i]
            i += 1
            k += 1

        # Inserting elements from right alist when elements from left alist are empty
        while j < len(right):
            alist[k] = right[j]
            j += 1
            k += 1
    return alist

def main():
    unsorted = [56,24,78,13,27,98,10,41]
    print(merge_sort_top_down(unsorted))
    
if __name__ == "__main__":
    main()