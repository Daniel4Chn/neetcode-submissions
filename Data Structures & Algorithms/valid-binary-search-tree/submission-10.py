# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        #go to deepest node left if 1 < root and root < right that is valid 
        #compare curr root to prev and prev would be the parent of that binary search tree
        arrayOfVals = []
        def dfs(root, prev):
            nonlocal arrayOfVals
            if not root:
                return 
            
            dfs(root.left, root)
            arrayOfVals.append(root.val)
            dfs(root.right, root)
        dfs(root, None)
        for i in range(len(arrayOfVals)):
            if i > 0:
                if arrayOfVals[i] <= arrayOfVals[i-1]:
                    return False
        return True
            
        
        
        