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
