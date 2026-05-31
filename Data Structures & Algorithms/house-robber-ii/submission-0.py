class Solution:
    def rob(self, nums: List[int]) -> int:
        if(len(nums) == 1):
            return nums[0]

        return max(self.helper(nums[:-1]), self.helper(nums[1:]))
        
    def helper(self, nums: List[int]) -> int:
        house1, house2 = 0, 0
        for num in nums:
            temp = max(house1 + num, house2)
            house1 = house2
            house2 = temp

        return house2
            


    