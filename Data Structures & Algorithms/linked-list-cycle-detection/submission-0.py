# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        tableOfNodes = set()

        trav = head
        while trav != None:
            if trav in tableOfNodes:
                return True
            else:
                tableOfNodes.add(trav)
                trav = trav.next
        
        return False