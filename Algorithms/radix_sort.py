def countingSort(alist, exp1):
    n = len(alist)

    # Creates final array to put sorted values into 
    sorted = [0] * n
    count = [0] * (10)

    # Mark all occurances in alist array
    for i in range(0, n):
        index = (alist[i]/exp1)
        count[(index)%10] += 1

    # Accumulatively add each index
    for i in range(1,10):
        count[i] += count[i-1]

    i = n-1  # Start at the end of alist
    while i >= 0:
        index = (alist[i]/exp1)
        sorted[count[(index) % 10] - 1] = alist[i]
        count[(index) % 10] -= 1
        i -= 1

    # Stores final output of count array into sorted array
    i = 0
    for i in range(0,len(alist)):
        alist[i] = sorted[i]

def radixSort(alist):
    max1 = max(alist)

    # Starts from least significant digit and progresses higher
    exp = 1
    while max1/exp > 0:
        countingSort(alist,exp)
        exp *= 10

    return alist


if __name__ == "__main__":
    alist = [170, 45, 75, 90, 802, 24, 2, 66] 
    print(radixSort(alist))
