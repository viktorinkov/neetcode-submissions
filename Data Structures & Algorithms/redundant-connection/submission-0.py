class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        n = len(edges)
        parent = [i for i in range(n + 1)]
        rank = [1 for i in range(n+1)]

        def find(node):
            p = parent[node]
            while p != parent[p]: # 1 with parent 2
                parent[p] = parent[parent[p]] # 1 with parent of parent of 1 i.e. parent of 2
                p = parent[p] # p parent of 2
            return p

        def union(n1, n2):
            p1, p2 = find(n1), find(n2)

            if p1 == p2:
                return False
            elif rank[p1] < rank[p2]:
                parent[p1] = p2
                rank[p2] += rank[p1]
            else:
                parent[p2] = p1
                rank[p1] += rank[p2]
            return True

        for n1, n2 in edges:
            if not union(n1, n2):
                return [n1, n2]