# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

# Solution using Floyd's Tortoise and Hare Algorithm
class Solution:
    '''
    LC 141:
    Given head, the head of a linked list, determine if the linked list has a cycle in it.
    There is a cycle in a linked list if there is some node in the list that can be reached again by continuously following the next pointer. Internally, pos is used to denote the index of the node that tail's next pointer is connected to. Note that pos is not passed as a parameter.
    Return true if there is a cycle in the linked list. Otherwise, return false.
    '''
    def hasCycle(self, head: ListNode) -> bool:
        if not head or not head.next:
            return False
        
        tortoise = head
        hare = head
        
        while hare and hare.next:
            tortoise = tortoise.next
            hare = hare.next.next
            if tortoise == hare:
                return True
        
        return False

    '''
    LC 142:
    Given a linked list, return the node where the cycle begins. If there is no cycle, return null.
    There is a cycle in a linked list if there is some node in the list that can be reached again by continuously following the next pointer. Internally, pos is used to denote the index of the node that tail's next pointer is connected to. Note that pos is not passed as a parameter.
    Notice that you should not modify the linked list.
    '''
    # Explanation: https://www.youtube.com/watch?v=9YTjXqqJEFE
    def detectCycle(self, head: ListNode) -> ListNode:
        if not head or not head.next:
            return None
        
        tortoise = head
        hare = head
        
        while hare and hare.next:
            tortoise = tortoise.next
            hare = hare.next.next
            
            if tortoise == hare:
                hare = head
                while tortoise != hare:
                    tortoise = tortoise.next
                    hare = hare.next
                return hare
        
        return None