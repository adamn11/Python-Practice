def bubbleSort(alist):
    # Starts from len(alist)-1 and goes to 0 because for each
    # runthrough, the largest number will be in its correct spot.
    # So there will be less comparisons needed each pass. 
    # For n items, there will be n-1 comparisons each time.
    for passnum in range(len(alist)-1,0,-1):
        for i in range(passnum):
            # Swap
            if alist[i]>alist[i+1]:
                temp = alist[i]
                alist[i] = alist[i+1]
                alist[i+1] = temp
    return alist

def main():
    arr = [6,1,4,2,7,8,9]
    print(bubbleSort(arr))

if __name__ == '__main__':
    main() 
