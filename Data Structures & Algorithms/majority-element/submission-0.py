class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        hashMap = {}
        maxCount = 0
        bestNum = 0
        for i in range(len(nums)):
            if(hashMap.get(nums[i])):
                hashMap[nums[i]] += 1
            else:
                hashMap[nums[i]] = 1
            if(hashMap[nums[i]] > maxCount):
                maxCount = hashMap[nums[i]]
                bestNum = nums[i]
        return bestNum