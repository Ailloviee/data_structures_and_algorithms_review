# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

# Solution using a pointer that collects smaller node of the two lists per iteration through the two lists
class Solution:
    '''
    LC 21:
    Merge two sorted linked lists and return it as a sorted list. 
    The list should be made by splicing together the nodes of the first two lists.
    '''
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        if not l1:
            return l2
        if not l2:
            return l1
        
        if l1.val < l2.val:
            head = l1
            l1 = l1.next
        else:
            head = l2
            l2 = l2.next
            
        p = head        
        
        while l1 or l2:
            if not l1:
                p.next = l2
                break
            if not l2:
                p.next = l1
                break
            if l1.val < l2.val:
                p.next = l1
                l1 = l1.next
            else:
                p.next = l2
                l2 = l2.next
            p = p.next
            
        
        return head