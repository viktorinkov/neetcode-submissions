class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        curr = nums[0]
        gl = nums[0]

        for num in nums[1:]:
            curr = max(curr + num, num)
            gl = max(curr, gl)
        
        return gl