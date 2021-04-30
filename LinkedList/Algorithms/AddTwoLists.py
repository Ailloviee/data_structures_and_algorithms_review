# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

# Solution using adder logic with carry
class Solution:
    '''
    LC 2:
    You are given two non-empty linked lists representing two non-negative integers. 
    The digits are stored in reverse order, and each of their nodes contains a single digit. 
    Add the two numbers and return the sum as a linked list.
    You may assume the two numbers do not contain any leading zero, except the number 0 itself.
    '''
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        sentinel = prev = ListNode(-1)
        
        c = 0
        while l1 or l2 or c != 0:
            if not l1 and not l2: 
                new_val = c
            elif not l1: 
                new_val = l2.val + c
                l2 = l2.next
            elif not l2: 
                new_val = l1.val + c
                l1 = l1.next
            else: 
                new_val = l1.val + l2.val + c
                l1 = l1.next
                l2 = l2.next
                
            if new_val >= 10:
                c = new_val // 10
                new_val = new_val % 10
            else:
                c = 0
            
            new_node = ListNode(new_val)
            prev.next = new_node
            prev = prev.next
        
        return sentinel.next