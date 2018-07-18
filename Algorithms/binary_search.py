def binary_search(array, target):
    min = 0
    max = len(array)

    while max >= min:
        #mid = min + (max - min) // 2
        mid = (max + min) // 2

        if array[mid] == target:
            return mid
        elif array[mid] > target:
            max = mid - 1
        elif array[mid] < target:
            min = mid + 1


def main():
    # TODO write case where target is not found
    array = [0, 14, 22, 54, 87]
    target = 87
    key = binary_search(array, target)

    print("Target %s is located at Index %s" % (target, key))


if __name__ == '__main__':
    main()
