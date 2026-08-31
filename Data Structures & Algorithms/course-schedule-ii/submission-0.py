class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        premap = {}
        for c, pre in prerequisites:
            if(c not in premap):
                premap[c] = []
            premap[c].append(pre)
        
        completed = set()
        path = []
        
        def dfs(c, visited):
            if(c in visited):
                return True

            visited.add(c)
            
            if c in premap:
                for pre in premap[c]:
                    if(pre in completed):
                        continue
                    elif(dfs(pre, visited)):
                        return True

            if(c not in completed):
                # add to path
                path.append(c)
            completed.add(c)
            return False
        
        for c in range(numCourses):
            if dfs(c, set()):
                return []

        return path
            