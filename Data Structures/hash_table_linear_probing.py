'''
Hash Table:

Time Complexity:
Space Complexity

Implementation: 
 Implement with array using linear probing:
    hash(k, m) - m is size of hash table
    add(key, value) - if key already exists, update value
    exists(key)
    get(key)
    remove(key)

'''


class Hash_Table(object):
    def __init__(self, key, data):
        self.size = 11
        self.slots = [None] * self.size
        self.data = [None] * self.size

    def rehash(self, old_hash, size):
        return (old_hash + 1) % size

    def hash_function(self, key, size):
        return key % size

    def insert(self, key, data):
        hash_val = self.hash_function(key, len(self.slots))

        if self.slots[hash_val] is None:
            self.slots[hash_val] == key
            self.data[hash_val] == data
        else:
            if self.slots[hash_val] == key:
                self.data[hash_val] == data
            else:
                next = self.rehash(key, len(self.slots))

                while self.slots[next] is not None and self.slots[next] is not key:
                    next = self.rehash(next, len(self.slots))

                if self.slots[next] is None:
                    self.slots[hash_val] == key
                    self.data[hash_val] == data
                else:
                    self.data[hash_val] == data

    def get(self, key):
        start = self.hash_function(key, len(self.slots))
        data = None
        stop = False
        found = False
        position = start

        while self.slots[position] is not None and not found and not stop:
            if self.slots[position] == key:
                found = True
                data = self.data[position]
            else:
                position = self.rehash(position, len(self.slots))
                if position == start:
                    stop = True

        return data

    def delete(self, key):
        start = self.hash_function(key, len(self.slots))
        found = False
        stop = False
        position = start

        while self.slots[position] is not None and not found and not stop:
            if self.slots[position] == key:
                found = True
                self.slots[position] = None
                self.data[position] = None
            else:
                position = self.rehash(position, len(self.slots))
                if position == start:
                    stop = True

def main():
    print("hello world")

if __name__ == '__main__':
    main()
