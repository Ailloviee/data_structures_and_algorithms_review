# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

# Solution using two pointers
class Solution:
    '''
    LC 206:
    Given the head of a singly linked list, reverse the list, and return the reversed list.
    '''
    def reverseList(self, head: ListNode) -> ListNode:
        if not head:
            return head
        
        prev = None
        
        while head:
            next_node = head.next
            head.next = prev
            prev = head
            head = next_node
        
        return prev