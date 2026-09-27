class TrieNode:
    def __init__(self):
        self.children = {}
        self.isEnd = False

class WordDictionary:

    def __init__(self):
        self.root = TrieNode()

    def addWord(self, word: str) -> None:
        curr = self.root
        for c in word:
            if c in curr.children:
                curr = curr.children[c]
            else:
                curr.children[c] = TrieNode()
                curr = curr.children[c]

        curr.isEnd = True
            

    def search(self, word: str) -> bool:
        def dfs(w, root):
            curr = root
            for i, c in enumerate(w):
                if c in curr.children:
                    curr = curr.children[c]
                elif c == ".":
                    for child in curr.children.values():
                        if dfs(w[i+1::], child):
                            return True
                    return False
                else:
                    return False
            
            return curr.isEnd
        return dfs(word, self.root)
        