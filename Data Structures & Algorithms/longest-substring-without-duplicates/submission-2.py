class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        myset = set()
        n = len(s)
        if(n == 0):
            return 0
        if(n == 1):
            return 1
        l = 0
        r = 0
        myset
        maxlen = 0
        while r < n:
            while(s[r] in myset):
                myset.remove(s[l])
                l += 1
            myset.add(s[r])
            maxlen = max(maxlen, r - l + 1)
            r += 1
        return maxlen