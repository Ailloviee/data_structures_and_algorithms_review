# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

# Solution using two pointers based on the math that both pointers will traverse the same distance to reach the intersection node
class Solution:
    '''
    LC 160:
    Given the heads of two singly linked-lists headA and headB, return the node at which the two lists intersect. 
    If the two linked lists have no intersection at all, return null.
    '''
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
        pA = headA
        pB = headB

        while pA != pB:
            pA = headB if pA is None else pA.next
            pB = headA if pB is None else pB.next
        
        return pA