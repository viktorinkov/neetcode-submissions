class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        map1 = {}

        for index, val in enumerate(nums):
            dif = target - val
            if(dif in map1):
                return [map1[dif], index]
            map1[val] = index
