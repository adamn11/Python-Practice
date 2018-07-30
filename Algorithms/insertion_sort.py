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