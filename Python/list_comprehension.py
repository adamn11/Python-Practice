# Simple example of list comprehension
def example1():
    list1 = [1,2,3,4,5,6,7,8,9]
    # List example
    # new_list1 = []
    # for x in list1:
    #     new_list1.append(x)
    # return new_list1

    # List Comprehension example
    return [x for x in list1]

# Multiplying every part of the list by 3
def example2():
    list2 = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    # List Example
    # new_list2 = []
    # for x in list2:
    #     new_list1.append(x*3)
    # return new_list2

    # List Comprehension example
    return [x*3 for x in list2]


def main():
    print(example1())
    print(example2())

if __name__ == "__main__":
    main()