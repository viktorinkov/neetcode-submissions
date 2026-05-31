class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        sol = {}
        n = len(nums)
        for i in range(n):
            sol[nums[i]] = 0
        for i in range(n):
            sol[nums[i]] += 1
        freqs = [[] for _ in range(n+1)]
        for num, freq in sol.items():
            freqs[freq].append(num)
        count = 0
        result = []
        for i in range(n, -1, -1):
            for num in freqs[i]:
                result.append(num)
                if len(result) == k:
                    return result

