class Solution:
    def canJump(self, nums: List[int]) -> bool:
        ## 1, 2, 0, 1, 0
        ## solve this with dp
        ## since we have only max jump
        goal = len(nums) - 1 ## last index
        for i in range(len(nums) - 2, -1, -1):
            ## we check if we can reach the goal
            if(nums[i] + i >= goal):
                goal = i
        
        return True if goal == 0 else False

        ## 