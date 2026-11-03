from collections import defaultdict
class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        graph = defaultdict(list)
        for pair in edges:
            parent = pair[0]
            child = pair[1]
            graph[parent].append(child)
            graph[child].append(parent)
        
        setOfVisited = set()
        def dfs(elem, parent):
            nonlocal setOfVisited
            if elem in setOfVisited:
                return False
        
            setOfVisited.add(elem)
            for i in graph[elem]:

                if i == parent:
                    continue

                if dfs(i, elem) == False:
                    return False
            
            return True
        
        if not dfs(0, -1):
            return False
        return len(setOfVisited) == n

