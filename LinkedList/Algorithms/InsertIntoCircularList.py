# Definition for singly-linked list.
class Node:
    def __init__(self, val=None, next=None):
        self.val = val
        self.next = next

# Solution using two pointers based on the math that both pointers will traverse the same distance to reach the intersection node
class Solution:
    '''
    LC 708:
    Given a node from a Circular Linked List which is sorted in ascending order, write a function to insert a value insertVal into the list such that it remains a sorted circular list. 
    The given node can be a reference to any single node in the list, and may not be necessarily the smallest value in the circular list.
    If there are multiple suitable places for insertion, you may choose any place to insert the new value. 
    After the insertion, the circular list should remain sorted.
    If the list is empty (i.e., given node is null), you should create a new single circular list and return the reference to that single node. 
    Otherwise, you should return the original given node.
    '''
    def insert(self, head: 'Node', insertVal: int) -> 'Node':
        new_node = Node(insertVal)
        
        if not head:
            new_node.next = new_node
            return new_node
        
        
        current = head
        
        while current:
            next_node = current.next
            # Normal scenario (new node's val in between two existing nodes' vals)
            if current.val <= insertVal <= next_node.val:
                break
            # When new node's val is less than the minimum or greater than the maximum val
            elif current.val > next_node.val and (insertVal >= current.val or insertVal <= next_node.val):
                break
            # When all nodes have been traversed (a full cycle) and none of the other scenarios have been triggered. This would be when all nodes are of the same value
            elif next_node == head:
                break
            else:
                current = next_node
        
        new_node.next = current.next
        current.next = new_node
        
        return head