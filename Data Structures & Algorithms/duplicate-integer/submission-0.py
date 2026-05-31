class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        count = {}
        n = len(nums)
        for i in range(n):
            if(nums[i] in count):
                count[nums[i]] += 1
            else:
                count[nums[i]] = 1
        for i in range(n):
            if(count[nums[i]] > 1):
                return True
        return False