class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        if(n != len(edges) + 1):
            return False

        # has cycle
        # is all connected

        adjList = [[] for _ in range(n)]
        # node = list of all connections
        for m, l in edges:
            adjList[m].append(l)
            adjList[l].append(m)

        visited = set()
        def bfs(i):
            q = deque()
            q.append((i, i))

            while q:
                curr, parent = q.popleft()
                visited.add(curr)
                for nei in adjList[curr]:
                    if(nei not in visited):
                        q.append((nei, curr))
                    elif(nei != parent and parent != curr):
                        return False # cycle
                
            return True # no cycle

        print(bfs(0))
        print(visited)
        print(len(visited))
        print("n is ")
        return bfs(0) and len(visited) == n

