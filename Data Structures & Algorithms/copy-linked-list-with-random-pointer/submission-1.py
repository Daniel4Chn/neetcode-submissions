"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        dummy = Node(0)
        setOfSeenNodes = {}
        trav = head
        while trav != None:
            setOfSeenNodes[trav] = Node(trav.val) 
            trav = trav.next

        trav = head
        trav2 = dummy
        while trav != None:
            trav2.next = setOfSeenNodes[trav]
            if trav.next != None:
                setOfSeenNodes[trav].next = setOfSeenNodes[trav.next]
            else:
                setOfSeenNodes[trav].next = None
            if trav.random != None:
                setOfSeenNodes[trav].random = setOfSeenNodes[trav.random]
            else:
                setOfSeenNodes[trav].random = None
            trav2 = trav2.next
            trav = trav.next
        return dummy.next

            
            
           
        
        
