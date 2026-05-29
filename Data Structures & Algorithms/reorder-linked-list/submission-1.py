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

        # IMPORTANT: split safely
        if prev:
            prev.next = None

        # reverse second half
        curr = slow
        rev = None

        while curr:
            temp = curr.next
            curr.next = rev
            rev = curr
            curr = temp

        # merge
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

        
        