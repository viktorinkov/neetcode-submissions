class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        prefix = [1] * n
        sufix = [1] * n
        
        for i in range(n):
            if(i != 0):
                prefix[i] = prefix[i-1] * nums[i-1]
            else:
                prefix[i] = 1

        for i in range(n-1, -1, -1):
            if(i != n-1):
                sufix[i] = sufix[i+1] * nums[i+1]
            else:
                sufix[i] = 1
        
        output = []
        for i in range(len(nums)):
            output.append(prefix[i] * sufix[i])

        return output