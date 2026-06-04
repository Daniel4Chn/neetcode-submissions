# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        
        carryValue = 0
        sumOfNodes = 0
        nodeValue = 0
        dummyNode = ListNode()
        currentNode = dummyNode
        while l1 or l2 or carryValue:
            if l1:
                v1 = l1.val
            else:
                v1 = 0
            if l2:
                v2 = l2.val
            else: 
                v2 = 0
            sumOfNodes = v1+v2+carryValue
            nodeValue = sumOfNodes % 10
            carryValue = sumOfNodes//10
            val = nodeValue
            newNode = ListNode(val)
            currentNode.next = newNode
            if l1:
                l1 = l1.next
            if l2:
                l2 = l2.next
            nodeValue = 0
            sumOfNodes = 0
            currentNode = currentNode.next

         

        return dummyNode.next
        

