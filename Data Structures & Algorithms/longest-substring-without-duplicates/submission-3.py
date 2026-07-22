class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l = 0
        myset = set()
        res = 0
        for r in range(len(s)):
            while(s[r] in myset):
                myset.remove(s[l])
                l += 1
            res = max(res, r - l + 1)
            myset.add(s[r])

        return res