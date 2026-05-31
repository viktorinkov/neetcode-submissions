class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        result = []
        n = len(nums)
        prefix = []
        p = 0
        for i in range(n):
            if(i == 0):
                p = nums[i]
            else:
                p *= nums[i]
            prefix.append(p)
        
        sufix = []
        s = 0
        for i in range(n - 1, - 1, -1):
            if(i == n - 1):
                s = nums[i]
            else:
                s *= nums[i]
            sufix.append(s)
        
        sufix.reverse()
        for i in range(n):
            if(i == 0):
                res = sufix[i+1]
            elif(i == n - 1):
                res = prefix[i-1]
            else:
                res = prefix[i-1] * sufix[i+1]
            result.append(res)
        return result