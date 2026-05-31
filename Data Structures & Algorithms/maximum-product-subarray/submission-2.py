class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        res = nums[0]

        maxProduct = nums[0]
        minProduct = nums[0]

        for i in range(1, len(nums)):
            tmp = maxProduct * nums[i]
            maxProduct = max(maxProduct * nums[i], minProduct * nums[i], nums[i])
            minProduct = min(tmp, minProduct * nums[i], nums[i])
            res = max(res, maxProduct)
        return res
