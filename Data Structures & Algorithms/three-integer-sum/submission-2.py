class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        ## from start to end num
        ## for nums[idx] try to find a a pair whose sum is 
        ## is -nums[idx] and both i,j > idx

        n = len(nums)
        res = []
        nums.sort()
        for i in range(n-2):
            targetSum = - nums[i]

            l, r = i+1, n-1
            while l < r:
                if(nums[l] + nums[r] > targetSum):
                    r -= 1
                elif(nums[l] + nums[r] < targetSum ):
                    l += 1
                else:
                    res.append([nums[i], nums[l], nums[r]])
                    r -=1
                    l +=1
        for i in range(len(res)-1):
            for j in range(len(res)-1, i, -1):
                if res[i] == res[j]:
                    del res[j]

        return res