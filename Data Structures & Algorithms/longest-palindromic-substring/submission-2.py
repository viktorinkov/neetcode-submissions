class Solution:
    def longestPalindrome(self, s: str) -> str:
        ## b a b a d
        ## b
        ## ba
        ## bab
        ## baba
        ## babad
        ## for each one we check is it a palindrome?
        ## 2 pointer

        res = ""
        maxL = 0
        ## what can we do
        n = len(s)
        if(n == 0):
            return ""
        if(n == 1):
            return s

        for i in range(n):
            ## case 1: length is odd
            currL = 0
            currS = ""

            l, r = i, i
            ## if odd
            while (l >= 0 and r <= n-1 and s[l] == s[r]):
                if(l == r):
                    currL = 1
                    currS = s[l]
                    l -= 1
                    r += 1
                    if(currL > maxL):
                        maxL = currL
                        res = currS
                    continue
                currL += 2
                currS = s[l] + currS
                currS = currS + s[r]
                if(currL > maxL):
                    maxL = currL
                    res = currS
                l -= 1
                r += 1
                
            ## if even
            currL = 0
            currS = ""
            l, r = i, i+1
            while (l >= 0 and r <= n-1 and s[l] == s[r]):
                currL += 2
                currS = s[l] + currS
                currS = currS + s[r]
                if(currL > maxL):
                    maxL = currL
                    res = currS
                l -= 1
                r += 1
        
        return res
