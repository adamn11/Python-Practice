def binary_search_recursive(array, target, min, max):
    mid = min + (max - min) / 2

    if array[mid] == target:
        return True
    elif array[mid] > target:
        return binary_search_recursive(array, target, min, mid-1)
    elif array[mid] < target:
        return binary_search_recursive(array, target, mid+1, max)

def main():
    array = [0, 1, 2, 3, 4]
    if binary_search_recursive(array,0,0,len(array)) is True:
        print "Yas"
    else:
        print "Nah"

if __name__ == '__main__':
    main()
