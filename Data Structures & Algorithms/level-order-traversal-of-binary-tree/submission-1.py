# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        q = deque()
        levels = []
        q.append(root)

        while q:
            currLevel = []
            length = len(q)
            for i in range(length):
                item = q.popleft()
                currLevel.append(item.val)
                if item.left:
                    q.append(item.left)
                if item.right:
                    q.append(item.right)
            levels.append(currLevel)
        
        return levels
