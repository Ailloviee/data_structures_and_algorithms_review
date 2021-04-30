# Definition for singly-linked list.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random

# Solution using two pointers based on the math that both pointers will traverse the same distance to reach the intersection node
class Solution:
    '''
    LC 138:
    A linked list of length n is given such that each node contains an additional random pointer, which could point to any node in the list, or null.
    Construct a deep copy of the list. The deep copy should consist of exactly n brand new nodes, where each new node has its value set to the value of its corresponding original node. 
    Both the next and random pointer of the new nodes should point to new nodes in the copied list such that the pointers in the original list and copied list represent the same list state. 
    None of the pointers in the new list should point to nodes in the original list.
    '''
    def copyRandomList(self, head: 'Node') -> 'Node':
        if not head:
            return head
        
        node_map = {}
        
        new_head = Node(head.val)
        node_map[head] = new_head
        original_cur = head
        copy_cur = Node(-1)
        
        
        while original_cur:
            # If the original node is already deep copied, do not create a new node
            if original_cur in node_map:
                new_node = node_map[original_cur]
            else:
                new_node = Node(original_cur.val)
                node_map[original_cur] = new_node
                
            # Link and get to the copied node    
            copy_cur.next = new_node
            copy_cur = copy_cur.next
            
            # If the random original node is already deep copied, do not create a new node
            if original_cur.random is not None:
                random_node = original_cur.random
                if random_node in node_map:
                    copy_cur.random = node_map[random_node]
                else:
                    new_node = Node(random_node.val)
                    copy_cur.random = new_node
                    node_map[random_node] = new_node
            
            original_cur = original_cur.next
        
        return new_head