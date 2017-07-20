def binary_search(array, target):
    min = 0
    max = len(array)

    while max > min:
        mid = min + (max - min) / 2

        if array[mid] == target:
            print "Found %s" % target
            break
        elif array[mid] > target:
            print "Nope"
            max = mid - 1
        elif array[mid] < target:
            print "Nope"
            min = target + 1

def main():
    array = [0, 1, 2, 3, 4]
    target = 0
    binary_search(array, target)

if __name__ == '__main__':
    main()








