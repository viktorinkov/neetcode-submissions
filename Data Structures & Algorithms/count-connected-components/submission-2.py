class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        visited = set()
        myDict = {}
        for i in range(len(edges)):
            if edges[i][0] not in myDict:
                myDict[edges[i][0]] = set()
            if edges[i][1] not in myDict:
                myDict[edges[i][1]] = set()

            myDict[edges[i][0]].add(edges[i][1])
            myDict[edges[i][1]].add(edges[i][0])
        
        def dfs(root):
            if(root in visited):
                return
            visited.add(root)
            if root in myDict:
                for nei in myDict[root]:
                    dfs(nei)
        ctn = 0
        for i in range(n):
            if(i not in visited):
                ctn += 1
                dfs(i)

        ## [[0,1], [1,2], [2,3], [4,5]]
        ## {0 : (1), 1 : (0, 2), 2 : (1, 3), 4 : (5), 5 : (4)}

        return ctn
