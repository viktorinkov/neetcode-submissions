class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)

        ## last house
        curr, prev = 0, 0

        for num in nums:
            temp = max(num + prev, curr)
            prev = curr
            curr = temp

        return curr

        