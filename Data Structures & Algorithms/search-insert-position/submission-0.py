class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        # binary tree
        l = 0
        r = len(nums) - 1
        while(l <= r):
            median = int((r - l) / 2) + l
            if(nums[median] == target):
                return median
            if(nums[median] > target):
                r = median - 1
            else:
                l = median + 1

        return l
