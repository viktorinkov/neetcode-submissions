class Solution:
    def countSubstrings(self, s: str) -> int:
        totalCount = 0
        n = len(s)

        for i in range(n):
            ## while odd
            l, r = i, i
            while(l >= 0 and r <= n - 1 and s[l] == s[r]):
                totalCount += 1
                l -= 1
                r += 1

            l, r = i, i+1
            while(l >= 0 and r <= n - 1 and s[l] == s[r]):
                totalCount += 1
                l -= 1
                r += 1

        return totalCount