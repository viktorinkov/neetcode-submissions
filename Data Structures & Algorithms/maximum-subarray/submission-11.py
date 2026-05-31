class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        if(len(nums) == 1):
            return nums[0]
        currSum = nums[0]
        maxSum = nums[0] 
        for i in range(1, len(nums)):
            currSum = max(currSum + nums[i], nums[i])
            if(currSum > maxSum):
                maxSum = currSum
        
        return maxSum

        ## 2
        ## (2 - 3, -3)
        ## (-1 + 4, 4)
        ## (4 - 2, -2)
        ## (2 + 2, 2)
        ## (4 + 1, 1)
        ## (5 -1, -1)
        ## (4 + 4, 4)
        ## 8
        