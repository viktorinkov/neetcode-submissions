class Trie:
    def __init__(self):
        self.children = {}
        self.word = None

    def addWord(self, word):
        cur = self
        for c in word:
            if c not in cur.children:
                cur.children[c] = Trie()
            cur = cur.children[c]
        cur.word = word

class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        root = Trie()
        for word in words:
            root.addWord(word)
        rows = len(board)
        cols = len(board[0])
        
        path = set()
        result = set()

        def dfs(row, col, node):
            if(row < 0 or col < 0 or row >= rows or col >= cols or ((row, col) in path)):
                return
            if(board[row][col] not in node.children):
                return
            else:
                ## continue through path of nodes
                path.add((row,col))
                ## update node
                node = node.children[board[row][col]]
                if node.word:
                    result.add(node.word)
                r1 = dfs(row + 1, col, node)
                r2 = dfs(row - 1, col, node)
                r3 = dfs(row, col + 1, node)
                r4 = dfs(row, col - 1, node)

                path.remove((row,col))
        
        for row in range(rows):
            for col in range(cols):
                dfs(row, col, root)

        return list(result)
                