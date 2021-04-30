
# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

# Solution using two pointers, start second pointer n steps later than the first pointer
# Careful for edge case: head might get deleted
class Solution:
    '''
    LC 19:
    Given the head of a linked list, remove the nth node from the end of the list and return its head.
    '''
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        p1 = head
        p2 = ListNode(-1, head)
        step = 0
        
        while p1:
            if step >= n:
                p2 = p2.next
            p1 = p1.next
            step += 1
        
        if p2.next == head: head = p2.next.next
        p2.next = p2.next.next
        return head