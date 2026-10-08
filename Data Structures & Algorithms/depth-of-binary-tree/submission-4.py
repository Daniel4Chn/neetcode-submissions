# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        
        #find a way to keep track of max depth while iterating through DFS
        maxVal = 0
        def dfs(root,value):
            nonlocal maxVal
            if not root:
                maxVal = max(maxVal, value)
                return None
            
            dfs(root.left,value+1)
            dfs(root.right,value+1)
        
        dfs(root,0)
        return maxVal
