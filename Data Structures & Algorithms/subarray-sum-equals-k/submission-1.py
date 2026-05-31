class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        prefix = {}
        res = 0
        curSum = 0
        for i in range(len(nums)):
            curSum += nums[i]
            if(curSum == k):
                res += 1
            res += prefix.get(curSum - k, 0)
            prefix[curSum] = prefix.get(curSum, 0) + 1
        return res
        