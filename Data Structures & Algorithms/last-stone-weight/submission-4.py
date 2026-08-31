class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        for i in range(len(stones)):
            stones[i] = -stones[i]

        heapq.heapify(stones)
        while len(stones) > 1:
            stone1 = - heapq.heappop(stones)
            stone2 = - heapq.heappop(stones)
            res = abs(stone1-stone2)
            if(res > 0):
                heapq.heappush(stones, -res)



        return -stones[0] if len(stones) > 0 else 0