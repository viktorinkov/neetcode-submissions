class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        premap = {}
        for course, prereq in prerequisites:
            if course not in premap:
                premap[course] = []
            premap[course].append(prereq)

        completed = set()
        def dfs(c, visited):
            if c in visited:
                return True

            visited.add(c)
            
            if c in premap:
                for prereq in premap[c]:
                    if(prereq in completed):
                        continue
                    else:
                        if dfs(prereq, visited):
                            return True

            completed.add(c)
            return False
        
        for i in range(numCourses):
            if dfs(i, set()):
                return False
        
        return True