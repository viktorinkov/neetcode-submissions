class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        ans = []
        n = len(nums)
        nums.sort()
        for i in range(n - 2):
            j = i + 1
            k = n - 1
            while j < k:
                cursum = nums[i] + nums[j] + nums[k]
                if(cursum > 0):
                    k -= 1
                elif(cursum < 0):
                    j += 1
                else:
                    if([nums[i], nums[j], nums[k]] in ans):
                        k -= 1
                        j += 1
                    else:
                        ans.append([nums[i], nums[j], nums[k]])

        return ans
