class Solution:
    def firstUniqChar(self, s: str) -> int:
        mydict = {}
        for char in s:
            if(mydict.get(char)):
                mydict[char] += 1
            else:
                mydict[char] = 1
        for i in range(len(s)):
            if(mydict[s[i]] == 1):
                return i
        return -1