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
        listOfNodes = []
        queueOfNodes = deque()
        queueOfNodes.append(root)
        while queueOfNodes:
            newList = []
            lengthOfList = len(queueOfNodes)
            for i in range(lengthOfList):
                item = queueOfNodes.pop()
                if item.left:
                    queueOfNodes.appendleft(item.left)
                if item.right:
                    queueOfNodes.appendleft(item.right)
                newList.append(item.val)
            listOfNodes.append(newList)
        return listOfNodes