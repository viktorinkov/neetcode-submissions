class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        map1 = {}
        maxVal = 0

        for num in nums:
            map1[num] = map1.get(num, 0) + 1
            maxVal = max(map1[num], maxVal)
        
        buck = [set() for _ in range(maxVal+1)]
        for num in nums:
            buck[map1[num]].add(num)
        
        ans = []
        for i in range(len(buck) - 1, 0,  - 1):
            for num in buck[i]:
                if(k > 0):
                    ans.append(num)
                    k -= 1


        return ans