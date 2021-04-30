# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

# Solution using two pointers and a sentinel node
class Solution:
    '''
    LC 203:
    Given the head of a linked list and an integer val, remove all the nodes of the linked list that has Node.val == val, and return the new head.
    '''
    def removeElements(self, head: ListNode, val: int) -> ListNode:
        if not head:
            return head
        
        dummy = ListNode(-1, head)
        prev = dummy
        
        while head:
            if head.val == val:
                prev.next = head.next
            else:
                prev = prev.next
            head = head.next
            
        return dummy.next