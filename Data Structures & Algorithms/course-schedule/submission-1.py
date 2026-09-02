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

        visited = set()
        cycleDetection = set()
        def dfs(elem):
            nonlocal visited
            nonlocal cycleDetection 
            if elem in cycleDetection:
                return False
            elif len(graph[elem]) == 0:
                return True
            cycleDetection.add(elem)
            for i in graph[elem]:
                if dfs(i) != True:
                    return False
            graph[elem] = []
            visited.add(elem)
            cycleDetection.remove(elem)
            return True

        for i in range(numCourses):
            value = dfs(i)
            if value == False:
                return False
        return True
        
            
        
            
            
            
            

