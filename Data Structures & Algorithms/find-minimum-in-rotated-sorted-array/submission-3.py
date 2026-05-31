class Solution:
    def findMin(self, nums: List[int]) -> int:
        n = len(nums)
        l, r = 0, len(nums) - 1
        res = []
        while l <= r:
            mid = (r + l) // 2
            res.append(mid)
            if(nums[mid] >= nums[r]):
                l = mid + 1
            else:
                r -= 1
        print(res)
        return nums[res[-1]]
                
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