'''

Bubble (Sinking) Sort: A simple sorting algorithm that repeatedly steps 
    through the list to be sorted, compares each pair of adjacent items 
    and swaps them if they are in the wrong order.

Time Complexity (Best): O(n)
Time Complexity (Average and Worst): O(n^2) 
Space Complexity: O(1)

Implementation:
Bubble Sort

'''


def bubblesort(arr):
    sorted = False

    while sorted != True:
        for i in arr:
            if arr[i] > arr[i+1]:
                # Swap
                temp = arr[i+1]
                arr[i+1] = arr[i]
                arr[i] = temp
            else:
                sorted = True
    return arr

def main():
    arr = [7,3,1,5,6,9,8,2,3]
    print(bubblesort(arr))

if __name__ == '__main__':
    main()