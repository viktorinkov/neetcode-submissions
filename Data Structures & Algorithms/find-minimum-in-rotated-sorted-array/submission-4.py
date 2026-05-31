class Solution:
    def findMin(self, nums: List[int]) -> int:
        n = len(nums)
        l, r = 0, len(nums) - 1
        res = 0
        while l <= r:
            mid = (r + l) // 2
            res = nums[mid]
            if(nums[mid] >= nums[r]):
                l = mid + 1
            else:
                r -= 1
        return res
                
## 3, 4, 5, 6, 1, 2
## l = 0
## r = 5
## mid = 2
## l = 3
## r = 5
## mid = 4
## l = 3
## r = 4
## mid = 3
## l = 4
## r = 4
## mid = 4