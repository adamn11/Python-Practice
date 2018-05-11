def seq_search(list, key):
    position = 0
    found = False

    while position < len(list) and not found:
        if list[position] == key:
            found = True
        else:
            position = position + 1

    return found


def main():
    list = [4, 5, 8, 2, 1, 4, 3]
    print(seq_search(list, 1))


if __name__ == "__main__":
    main()
