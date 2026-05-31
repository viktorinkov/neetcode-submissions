class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        ## undirected edges
        ## n nodes
        ## each node must have only one parent
        ## [[0, 1], [0, 2], [0, 3], [1, 4]]
        
        ## we want to avoid cycles
        ## we want one parent only
        
        ## what is a way to detect a cycle
        ## neighbors map
        neighbors = {}
        for i in range(n):
            neighbors[i] = []
        for edge in edges:
            neighbors[edge[0]].append(edge[1])
            neighbors[edge[1]].append(edge[0])
        
        visits = set()

        def dfs(node, par):
            if node in visits:
                return False
            visits.add(node)
            for nei in neighbors[node]:
                if(nei == par):
                    continue
                if(dfs(nei, node) == False):
                    return False
            return True
        
        return dfs(0, -1) and len(visits) == n

        
            
