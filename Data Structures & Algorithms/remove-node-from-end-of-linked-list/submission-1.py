# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        countOfNodes = 0
        trav = head
        while trav:
            countOfNodes+=1
            trav = trav.next
        if countOfNodes == 1:
            return None
        trav2 = head
        countOfNodes -= n
        if countOfNodes == 0:
            return head.next
        prev = None
        while trav2 and countOfNodes > 0:
            countOfNodes-=1
            prev = trav2
            trav2 = trav2.next
        prev.next = trav2.next
        trav2.next = None
        return head
        
