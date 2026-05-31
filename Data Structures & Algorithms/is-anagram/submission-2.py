class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        dicto = {}
        reserve = {}
        n = len(s)
        m = len(t)
        for i in range(n):
            if(s[i] in dicto):
                dicto[s[i]] += 1
            else:
                dicto[s[i]] = 1
        for i in range(m):
            if(t[i] in reserve):
                reserve[t[i]] += 1
            else:
                reserve[t[i]] = 1
        if(dicto == reserve):
            return True
        return False
        