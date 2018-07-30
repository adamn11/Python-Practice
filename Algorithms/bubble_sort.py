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