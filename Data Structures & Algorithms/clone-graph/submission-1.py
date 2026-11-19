"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        oldToNew = {}
        copyOfNode = node
        if not node:
            return None
        q = deque()
        q.append(node)
        oldToNew[node] = Node(node.val)
        while q:
            length = len(q)
            for i in range(length):
                curr_node = q.popleft()
                for neighbor in curr_node.neighbors:
                    if neighbor not in oldToNew:
                        oldToNew[neighbor] = Node(neighbor.val)
                        q.append(neighbor)
                    
                    oldToNew[curr_node].neighbors.append(oldToNew[neighbor])

        return oldToNew[copyOfNode]





        