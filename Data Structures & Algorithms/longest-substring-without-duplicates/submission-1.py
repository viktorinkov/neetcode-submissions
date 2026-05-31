class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        found = set()
        l = 0
        res = 0

        for r in range(len(s)):
            while s[r] in found:
                found.remove(s[l])
                l += 1
            found.add(s[r])
            res = max(res, r - l + 1)
        return res