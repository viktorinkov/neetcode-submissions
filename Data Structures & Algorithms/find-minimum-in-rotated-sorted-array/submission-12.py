class Solution:
    def findMin(self, nums: List[int]) -> int:
        n = len(nums)
        if(n == 1):
            return nums[0]
        if(n == 2):
            return min(nums)
        
        l = 0
        r = n - 1
        res = nums[0]
        while l <= r:
            if(nums[l] < nums[r]):
                res = min(res, nums[l])
                break

            m = (l + r) // 2
            res = min(res, nums[m])

            if(nums[m] >= nums[l]):
                l = m + 1
            else:
                r = m - 1

        return res