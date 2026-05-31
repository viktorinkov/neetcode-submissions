class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        mymap = {}
        for i in range(len(nums)):
            mymap[nums[i]] = mymap.get(nums[i], 0) + 1
            if(mymap[nums[i]] > 1):
                return True
        return False