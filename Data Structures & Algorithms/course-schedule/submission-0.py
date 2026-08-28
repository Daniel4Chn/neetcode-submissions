from collections import defaultdict
class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        #create a DAG based off of the array
        graph = defaultdict(list)
        for i in range(len(prerequisites)):
            dependentCourse = prerequisites[i][1]
            course = prerequisites[i][0]
            graph[course].append(dependentCourse)
            if dependentCourse not in graph:
                graph[dependentCourse] = []
        visiting = set()
        def dfs(graph, val):
            if val in visiting:
                return False

            if len(graph[val]) == None:
                return True
            visiting.add(val)
            for elem in graph[val]:
                if dfs(graph, elem) == False:
                    return False
            visiting.remove(val)
            graph[val] = []
            return True

        for v in range(numCourses):
            if not dfs(graph, v):
                return False
        
        return True
            
        
            
            
            
            

