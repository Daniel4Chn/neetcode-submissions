from collections import defaultdict
class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        #n nodes labeled from 0 to n-1. You are given an integer n and an array edges where edges[i] = [ai, bi] edge between ai and bi we have to find the numberOfConnected components


        connectedComponents = 0
        graph = defaultdict(list)
        for edge in edges:
            edge1 = edge[0]
            edge2 = edge[1]
            graph[edge1].append(edge2)
            graph[edge2].append(edge1)
        
        for i in range(n):
            if i not in graph:
                graph[i] = []

        visited = set()
        def dfs(elem, parent):
            if elem in visited:
                return
            
            visited.add(elem)
            for children in graph[elem]:
                if children == parent:
                    continue
                dfs(children, elem)

        
        dfs(0, -1)
        connectedComponents +=1
        for num in graph:
            if num not in visited:
                dfs(num, -1)
                connectedComponents+=1
        return connectedComponents


