# Definition for singly-linked list.
class Node:
    def __init__(self, val, prev, next, child):
        self.val = val
        self.prev = prev
        self.next = next
        self.child = child

# Solution using DFS with recursion
class Solution:
    '''
    LC 430:
    You are given a doubly linked list which in addition to the next and previous pointers, it could have a child pointer, which may or may not point to a separate doubly linked list. 
    These child lists may have one or more children of their own, and so on, to produce a multilevel data structure, as shown in the example below.
    Flatten the list so that all the nodes appear in a single-level, doubly linked list. You are given the head of the first level of the list.
    '''
    def flatten(self, head):
        if not head:
            return head

        # pseudo head to ensure the `prev` pointer is never none
        pseudoHead = Node(None, None, head, None)
        self.flatten_dfs(pseudoHead, head)

        # detach the pseudo head from the real head
        pseudoHead.next.prev = None
        return pseudoHead.next


    def flatten_dfs(self, prev, curr):
        """ return the tail of the flatten list """
        if not curr:
            return prev

        curr.prev = prev
        prev.next = curr

        # the curr.next would be tempered in the recursive function
        tempNext = curr.next
        tail = self.flatten_dfs(curr, curr.child)
        curr.child = None
        return self.flatten_dfs(tail, tempNext)

# Another solution would be DFS iteration method using a stack (do work, push right(curr.next), then push left(curr.child))
    # def flatten(self, head):
    #     if not head:
    #         return

    #     pseudoHead = Node(0,None,head,None)
    #     prev = pseudoHead

    #     stack = []
    #     stack.append(head)

    #     while stack:
    #         curr = stack.pop()

    #         prev.next = curr
    #         curr.prev = prev

    #         if curr.next:
    #             stack.append(curr.next)

    #         if curr.child:
    #             stack.append(curr.child)
    #             # don't forget to remove all child pointers.
    #             curr.child = None

    #         prev = curr
    #     # detach the pseudo head node from the result.
    #     pseudoHead.next.prev = None
    #     return pseudoHead.next
