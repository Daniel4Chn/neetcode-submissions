from collections import defaultdict
class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        graph = defaultdict(list)
        for arr in prerequisites:
            course = arr[1]
            dependentCourse = arr[0]
            graph[dependentCourse].append(course)
            if course not in graph:
                graph[course] = []
        res = []
        visited = set()
        cycleDetection = set()
        def dfs(elem):
            
            if elem in cycleDetection:
                return False
            if elem in visited:
                return True
            cycleDetection.add(elem)
            for i in graph[elem]:
                if dfs(i) != True:
                    return False
            graph[elem] = []
            visited.add(elem)
            cycleDetection.remove(elem)
            res.append(elem)
            return True

        for i in range(numCourses):
            if dfs(i) == False:
                return []
        return res

        