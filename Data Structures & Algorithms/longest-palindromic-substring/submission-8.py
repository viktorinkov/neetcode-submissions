class Solution:
    def longestPalindrome(self, s: str) -> str:
        n = len(s)
        cache = [[False for x in range(n)] for y in range(n)]

        # mark all single ones as True
        resIdx = 0
        resLen = 0

        def dp(i, j):
            # need to add bounds
            nonlocal resLen, resIdx
            if(i == j or (s[i] == s[j] and (j - i == 1 or cache[i+1][j-1]))):
                cache[i][j] = True
            if cache[i][j]:
                l = j - i + 1
                if resLen < l:
                    resLen = l
                    resIdx = i

        for j in range(n):
            for i in range(j + 1):
                dp(i, j)

        return s[resIdx:resIdx+resLen]       

