"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node:
            return None
        oldToNew = {}
        q = deque()
        q.append(node)
        oldToNew[node] = Node(node.val)

        while q:
            lengthOfQ = len(q)
            for i in range(lengthOfQ):
                value = q.popleft() 
                for j in value.neighbors:
                    if j not in oldToNew:
                        oldToNew[j] = Node(j.val)
                        q.append(j)
                    oldToNew[value].neighbors.append(oldToNew[j])
                    
        
        return oldToNew[node]





        