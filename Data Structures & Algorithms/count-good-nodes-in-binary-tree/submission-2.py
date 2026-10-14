from collections import deque
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        
        #in bfs every level = first time that specific node was found by another node so its the shortest path that node assuming unweighted graph
        #store max of previously seen node??? so if the child of that node is greater than the previously maxed node in that path, you add that 
        numOfGood = 0
        q = deque()
        q.append((root,-101))

        while q:
            length = len(q)
            
            for i in range(length):
                item = q.popleft()
                val = item[0]
                maxVal = item[1]
                if val.val >= maxVal:
                    numOfGood +=1
                if val.left:
                    q.append((val.left, max(val.val,maxVal)))
                if val.right:
                    q.append((val.right, max(val.val,maxVal)))
                
                
        return numOfGood
