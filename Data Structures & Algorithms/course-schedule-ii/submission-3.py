from collections import defaultdict

class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        valid = []
        graph = defaultdict(list)

        for dependent, course in prerequisites:
            graph[course].append(dependent)

        for num in range(numCourses):
            if num not in graph:
                graph[num] = []

        visitingSet = set()
        visitedSet = set()

        def dfs(elem):
            if elem in visitingSet:
                return False

            if elem in visitedSet:
                return True

            visitingSet.add(elem)

            for potential in graph[elem]:
                if not dfs(potential):
                    return False

            visitingSet.remove(elem)
            visitedSet.add(elem)
            valid.append(elem)

            return True

        for value in graph:
            if not dfs(value):
                return []

        return valid[::-1]