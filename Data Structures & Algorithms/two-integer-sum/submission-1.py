class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        n = len(nums)
        dic = {}
        for i in range(n):
            difference = target - nums[i]
            if(difference in dic):
                return [dic[difference], i]
            else:
                dic[nums[i]] = i
        return []