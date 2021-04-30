# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

# Solution using two pointers 
class Solution:
    '''
    LC 328:
    Given the head of a singly linked list, group all the nodes with odd indices together followed by the nodes with even indices, and return the reordered list.
    '''
    def oddEvenList(self, head: ListNode) -> ListNode:
        if not (head and head.next):
            return head
        
        odd_head = head
        even_head = head.next
        feven_head = even_head
        
        
        while odd_head.next and even_head.next:
            odd_head.next = even_head.next
            even_head.next = odd_head.next.next
            odd_head = odd_head.next
            even_head = even_head.next
        
        odd_head.next = feven_head
        
        return head