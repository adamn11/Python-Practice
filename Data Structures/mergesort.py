# Top-down Implementation
def mergeSort(array):
    if len(array) > 1:
        mid = len(array) // 2
        left = array[:mid]
        right = array[mid:]

        mergeSort(left)
        mergeSort(right)

        i = 0 # Index for left array
        j = 0 # Index for right array
        k = 0 # Index for original array

        # Comparing left and right array and inserting the smallest one into original array
        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                array[k] = left[i]
                i += 1
            else:
                array[k] = right[j]
                j += 1
            k += 1
        
        # Inserting elements from left array when elements from right array are empty
        while i < len(left):
            array[k] = left[i]
            i += 1
            k += 1

        # Inserting elements from right array when elements from left array are empty
        while j < len(right):
            array[k] = right[j]
            j += 1
            k += 1
    return array

def main():
    unsorted = [56,24,78,13,27,98,10,41]
    print(mergeSort(unsorted))
    
if __name__ == "__main__":
    main()