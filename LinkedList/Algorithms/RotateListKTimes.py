# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

# Solution using two pointers
class Solution:
    '''
    LC 61:
    Given the head of a linked list, rotate the list to the right by k places.
    '''
    def rotateRight(self, head: ListNode, k: int) -> ListNode:
        if not head:
            return head
        
        # prev = ListNode(-1, head)
        tail = head
        size = 1
        
        while tail.next:
            size += 1
            # prev = prev.next
            tail = tail.next
        
        if tail == head:
            return head
        
        for _ in range(size - (k % size)):
            tail.next = head
            next_node = head.next
            head.next = None
            head = next_node
            tail = tail.next
        
        return head