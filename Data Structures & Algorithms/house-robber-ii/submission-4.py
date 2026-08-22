class Solution:
    def rob(self, nums: List[int]) -> int:
        l = len(nums)
        if l == 1:
            return nums[0]

        def helper(array):
            first = 0
            second = 0
            for n in array:
                temp = max(n + first, second)
                first = second
                second = temp
            return second
    
        return max(helper(nums[0:l-1]), helper(nums[1:l]))