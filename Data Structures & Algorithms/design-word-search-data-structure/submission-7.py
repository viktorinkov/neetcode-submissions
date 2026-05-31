class Trie:
    def __init__(self):
        self.children = {} ## a map with pairs of key - char and val - node
        self.endOfWord = False ## boolean that tells us if it is the end of a word


class WordDictionary:
    def __init__(self):
        self.root = Trie()
        

    def addWord(self, word: str) -> None:
        cur = self.root

        for c in word:
            if(c not in cur.children):
                cur.children[c] = Trie()
            cur = cur.children[c]

        cur.endOfWord = True
        

    def search(self, word: str) -> bool:
        def dfs(depth, root):
            cur = root
            for i in range(depth, len(word)):
                if(word[i] == "."):
                    for child in cur.children.values():
                        if(dfs(i+1, child)):
                            return True
                    return False
                else:
                    if(word[i] not in cur.children):
                        return False
                    cur = cur.children[word[i]]
            return cur.endOfWord
        return dfs(0, self.root)
                            
