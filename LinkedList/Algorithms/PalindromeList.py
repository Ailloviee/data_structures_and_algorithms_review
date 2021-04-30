# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

# Solution using a list to record a traversal, then check if list = list's reverse
class Solution:
    '''
    LC 234:
    Given the head of a singly linked list, return true if it is a palindrome.
    '''
    def isPalindrome(self, head: ListNode) -> bool:
        l = []
        
        current = head
        while current:
            l.append(current.val)
            current = current.next    
        
        return l == l[::-1]

# Another solution would be using two pointers and recursive. (One pointer goes to end, then comes back while comparing value with another pointer starting at head of list)
#         self.front = head
        
#         def recursive(current=head):
#             if current:
#                 if not recursive(current.next):
#                     return False
#                 if self.front.val != current.val:
#                     return False
#                 self.front = self.front.next
#             return True
        
#         return recursive()