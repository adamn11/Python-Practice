def binary_serach(key,array,min,max):
    if min > max:
        return False
    else:
        midpoint = find_midpoint(array,min,max)

    if array[midpoint] < key:
        binary_serach(key,array,array[midpoint+1],max)
    elif array[midpoint] > key:
        binary_serach(key,array,min,array[midpoint-1])
    else:
        return True

def find_midpoint(array,min,max):
    midpoint = (array.index(max) - array.index(min)) / 2
    return array.index(min) + midpoint


def main():
    array = [0,1,2,3,5,8,14,29,64,99,192,208,344]

    if binary_serach(5,array,0,344):
        print 'Yas'
    else:
        print 'Nah'

if __name__ == '__main__':
    main()
