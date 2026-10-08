# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        #track max level using BFS so each level is one depth
        if root == None:
            return 0
        q = deque()
        q.append(root)
        depth = 0
        while q:
            length = len(q)
            print(q)
            for i in range(length):
                curr = q.popleft()
                if curr.left:
                    q.append(curr.left)
                if curr.right:
                    q.append(curr.right)
            depth+=1
        return depth
