class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        dist = []
        x2, y2 = 0, 0
        for point in points:
            x1 = point[0]
            y1 = point[1]
            temp = math.sqrt((x1 - x2)**2 + (y1 - y2)**2)
            heapq.heappush(dist, [temp, point])
        
        res = []
        for _ in range(k):
            d, point = heapq.heappop(dist)
            res.append(point)

        return res
        

