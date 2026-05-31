class Node:
    def __init__(self):
        self.children = {}
        self.isEnd = False

class PrefixTree:
    def __init__(self):
        self.root = Node()

    def insert(self, word: str) -> None:
        cur = self.root
        for char in word:
            if(char not in cur.children):
                cur.children[char] = Node()
            cur = cur.children[char]
        cur.isEnd = True

    def search(self, word: str) -> bool:
        cur = self.root
        for char in word:
            if char not in cur.children:
                return False
            else:
                cur = cur.children[char]
        return True if cur.isEnd == True else False

    def startsWith(self, prefix: str) -> bool:
        cur = self.root
        for char in prefix:
            if char not in cur.children:
                return False
            else:
                cur = cur.children[char]
        return True

        
        