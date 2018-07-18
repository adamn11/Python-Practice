def list_practice():
    myList = [1, 7, 3, 2, 6, 8]
    print(myList)

    print("List Length: ", len(myList))
    myList.insert(2, 2)
    myList.sort()
    print(myList)

    print(myList.index(2))

    myList.remove(2)
    print(myList)

def main():
    list_practice()

if __name__ == '__main__':
    main()
