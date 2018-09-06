def binary_search(alist, target):
    min = 0
    max = len(alist)

    while max >= min:
        #mid = min + (max - min) // 2
        mid = (max + min) // 2

        if alist[mid] == target:
            return mid
        elif alist[mid] > target:
            max = mid - 1
        elif alist[mid] < target:
            min = mid + 1

def main():
    # TODO write case where target is not found
    alist = [0, 14, 22, 54, 87]
    target = 87
    key = binary_search(alist, target)

    print("Target %s is located at Index %s" % (target, key))

if __name__ == '__main__':
    main()
