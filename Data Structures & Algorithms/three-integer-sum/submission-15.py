class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        ans = []
        n = len(nums)
        nums.sort()
        for i in range(n - 2):
            if(i > 0 and nums[i] == nums[i-1]):
                continue

            j = i + 1
            k = n - 1
            while j < k:
                # need extra case
                cursum = nums[i] + nums[j] + nums[k]
                if(cursum > 0):
                    k -= 1
                elif(cursum < 0):
                    j += 1
                else:
                    ans.append([nums[i], nums[j], nums[k]])
                    j += 1
                    k -= 1
                    while nums[j] == nums[j - 1] and j < k:
                        j += 1

        return ans
