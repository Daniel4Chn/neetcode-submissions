# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        pValues = []
        qValues = []
        def dfs1(root):
            nonlocal pValues
            if not root:
                pValues.append(None)
                return
            pValues.append(root.val)
            dfs1(root.left)
            dfs1(root.right)
        def dfs2(root):
            nonlocal qValues
            if not root:
                qValues.append(None)
                return
            qValues.append(root.val)
            dfs2(root.left)
            dfs2(root.right)
        
        dfs1(p)
        dfs2(q)

        return pValues == qValues