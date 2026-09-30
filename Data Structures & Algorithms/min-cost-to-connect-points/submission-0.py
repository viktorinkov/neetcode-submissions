class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        # calculate all edges
        # add minimum edge that connects a new point

        def findDist(pi, pj):
            xi, yi = pi
            xj, yj = pj
            return abs(xi - xj) + abs(yi - yj)

        edge = defaultdict(list)

        # O(n^2)
        for i in range(len(points)):
            for j in range(len(points)):
                if i == j:
                    continue
                edge[i].append((findDist(points[i], points[j]), j)) # (dist, pointId)
        
        res = 0
        visited = set()
        minHeap = [(0, 0)] # dist, pointId

        while minHeap:
            d1, p1 = heapq.heappop(minHeap)
            if p1 in visited:
                continue

            visited.add(p1)
            res += d1
            for d2, p2 in edge[p1]:
                if p2 not in visited:
                    heapq.heappush(minHeap, (d2, p2))
        
        return res
