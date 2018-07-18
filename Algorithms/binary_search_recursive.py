def binary_search_recursive(array, target, min, max):
    mid = min + (max - min) // 2

    if array[mid] == target:
        return mid
    elif array[mid] > target:
        return binary_search_recursive(array, target, min, mid-1)
    elif array[mid] < target:
        return binary_search_recursive(array, target, mid+1, max)

def main():
    # TODO write case where target is not found
    array = [0, 22, 46, 67, 100]
    target =100
    key = binary_search_recursive(array, target, 0, len(array))
    print("Target %d is located at Index %d" % (target, key))

if __name__ == '__main__':
    main()
