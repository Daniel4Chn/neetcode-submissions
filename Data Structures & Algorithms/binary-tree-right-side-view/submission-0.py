from collections import deque
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
        rightSideView = []
        unTouchedNodes = deque()
        unTouchedNodes.append(root)

        while unTouchedNodes:
            currentLevel = []
            lengthOfLevel = len(unTouchedNodes)
            for i in range(lengthOfLevel):
                currentNode = unTouchedNodes.popleft()
                if currentNode.left:
                    unTouchedNodes.append(currentNode.left)
                if currentNode.right:
                    unTouchedNodes.append(currentNode.right)
                currentLevel.append(currentNode)
            if currentLevel:
                rightSideView.append(currentLevel[-1].val)
        return rightSideView