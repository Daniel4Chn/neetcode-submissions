# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:

        if not head or not head.next:
            return

        slow = head
        fast = head
        prev = None

        while fast and fast.next:
            prev = slow
            slow = slow.next
            fast = fast.next.next

        if prev:
            prev.next = None

        curr = slow
        rev = None

        while curr:
            temp = curr.next
            curr.next = rev
            rev = curr
            curr = temp

        first = head
        second = rev

        while second and first:
            t1 = first.next
            t2 = second.next

            first.next = second
            if t1:
                second.next = t1
            
            first = t1
            second = t2

        
        