class TrieNode:
    def __init__(self):
        self.children = [None] * 26  # Holds all the letters in the alphabet
        self.isEndOfWord = False


class Trie:
    def __init__(self):
        self.root = self.getNode()

    def getNode(self):
        # Creates and returns a new trie node (initialized to NONE)
        return TrieNode()

    def _charToIndex(self,ch): 
        # private helper function 
        # Converts key current character into index 
        # use only 'a' through 'z' and lower case 
        return ord(ch)-ord('a') 

    def insert(self, key):
        current = self.root

        for x in range(len(key)):
            index = self._charToIndex(key[x])

            if not current.children[index]:
                current.children[index] = self.getNode()
            current = current.children[index]

        current.isEndOfWord = True

    def search(self, key):
        current = self.root

        for x in range(len(key)):
            index = self._charToIndex(key[x])

            if not current.children[index]:
                return False
            current = current.children[index]

        return current != None and current.isEndOfWord


def main(): 
    # Input keys (use only 'a' through 'z' and lower case) 
    keys = ["the","a","there","anaswe","any", 
            "by","their"] 
    output = ["Not present in trie", 
              "Present in tire"] 

    t = Trie() 
  
    # Construct trie 
    for key in keys: 
        t.insert(key) 
  
    print("{} ---- {}".format("the",output[t.search("the")])) 
    print("{} ---- {}".format("these",output[t.search("these")])) 
    print("{} ---- {}".format("their",output[t.search("their")])) 
    print("{} ---- {}".format("thaw",output[t.search("thaw")])) 
  
if __name__ == '__main__': 
    main() 