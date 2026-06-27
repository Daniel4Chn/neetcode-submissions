from collections import deque
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        if not root:
            return 0

        countOfGood = 0

        nodes = deque()
        nodes.append((root, -101))
        
        while nodes:
            
            length = len(nodes)
            for i in range(length):
                curr = nodes.popleft()
                if curr[0].left:
                    nodes.append((curr[0].left, max(curr[0].val, curr[-1])))
                if curr[0].right:
                    nodes.append((curr[0].right, max(curr[0].val, curr[-1])))
                
                if curr[0].val >= curr[1]:
                    countOfGood+=1
            
        return countOfGood 
            




            