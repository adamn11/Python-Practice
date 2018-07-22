def quicksort(alist):
    quicksorthelper(alist, 0, len(alist)-1)

def quicksorthelper(alist, first, last):
    if first < last:
        index = partition(alist, first, last)
        quicksorthelper(alist, first, index-1)
        quicksorthelper(alist, index+1, last)

def partition(alist, first, last):
    pivot = alist[first]
    left_index = first + 1
    right_index = last
    done = False

    while not done:
        # Keep moving left index element is greater than pivot
        while alist[left_index] <= pivot and left_index <= right_index:
            left_index += 1

        # Keep moving right index until element is less than pivot
        while alist[right_index] >= pivot and right_index >= left_index:
            right_index -= 1

        if right_index < left_index:
            done = True
        else:
            # Swap out of order elements
            temp = alist[left_index]
            alist[left_index] = alist[right_index]
            alist[right_index] = temp
    
    # Swap pivot with right index
    temp = alist[first]
    alist[first] = alist[right_index]
    alist[right_index] = temp

    return right_index

def main():
    arr = [6,4,1,3,9,8,7,2]
    quicksort(arr)
    print(arr)

if __name__ == "__main__":
    main()
