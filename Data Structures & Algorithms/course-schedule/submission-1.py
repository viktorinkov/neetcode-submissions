class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        ## you must finish b before a
        ## directional
        ## acyclical
        ## DAG

        ## we need to detect a cycle
        ## if there is a cycle, then false
        ## END: check if all nodes are connected

        ## group by nodes
        preMap = {}
        for i in range(numCourses):
            preMap[i] = []
        for i in range(len(prerequisites)):
            preMap[prerequisites[i][0]].append(prerequisites[i][1])

        visited = set()

        def dfs(courseId):
            if(courseId in visited):
                return False
            if(preMap[courseId] == []):
                return True
            ## check if a prereq has been visited
            visited.add(courseId)
            for parentId in preMap[courseId]:
                if not dfs(parentId):
                    return False
            visited.remove(courseId)
            preMap[courseId] = []
            return True

        for courseId in range(numCourses):
            if courseId not in visited:
                if(dfs(courseId) == False):
                    return False
        
        return True
            
            