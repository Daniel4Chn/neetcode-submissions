from collections import defaultdict
class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:

        graph = defaultdict(list)
        for arr in prerequisites:
            course = arr[0]
            dependentCourse = arr[1]
            graph[dependentCourse].append(course)
            if course not in graph:
                graph[course] = []
        visitingSet = set()

        def dfs(elem):
            nonlocal visitingSet
            if graph[elem] == []:
                return True
            if elem in visitingSet:
                return False
            visitingSet.add(elem)
            for var in graph[elem]:
                if dfs(var) == False:
                    return False
            visitingSet.remove(elem)
            graph[elem] = []
            return True
            
            
        
        for course in graph:
            if dfs(course) == False:
                return False
        return True
            
            
            

