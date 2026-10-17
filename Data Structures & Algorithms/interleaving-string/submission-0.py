class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        l1 = len(s1)
        l2 = len(s2)
        a = len(s3)
        if l1 + l2 != a:
            return False

        cache = {}

        def dfs(i, j):
            if (i, j) in cache:
                return cache[(i, j)]

            if i == l1 and j == l2:
                return True
            
            if i < l1 and s1[i] == s3[i + j] and dfs(i + 1, j):
                return True
            
            if j < l2 and s2[j] == s3[i + j] and dfs(i, j + 1):
                cache[(i, j)] = True
                return True
            
            cache[(i, j)] = False
            return False
        
        return dfs(0, 0)