from collections import deque
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# Solution using DFS recursive
class Solution:
    '''
    LC 116 / 117
    '''
    def connect(self, root: 'Node') -> 'Node':
        levels = []
        
        def DFS(node, level):
            if not node:
                return
            
            if level == len(levels):
                levels.append([])
            
            levels[level].append(node)
            
            DFS(node.left, level + 1)
            DFS(node.right, level + 1)
            
        DFS(root, 0)
        
        for level in levels:
            for idx in range(len(level)-1):
                level[idx].next = level[idx+1]
        
        return root

# Solution that uses constant space and iterative
    # def connect(self, root: 'Node') -> 'Node':
        
    #     if not root:
    #         return root
        
    #     # Initialize a queue data structure which contains
    #     # just the root of the tree
    #     Q = collections.deque([root])
        
    #     # Outer while loop which iterates over 
    #     # each level
    #     while Q:
            
    #         # Note the size of the queue
    #         size = len(Q)
            
    #         # Iterate over all the nodes on the current level
    #         for i in range(size):
                
    #             # Pop a node from the front of the queue
    #             node = Q.popleft()
                
    #             # This check is important. We don't want to
    #             # establish any wrong connections. The queue will
    #             # contain nodes from 2 levels at most at any
    #             # point in time. This check ensures we only 
    #             # don't establish next pointers beyond the end
    #             # of a level
    #             if i < size - 1:
    #                 node.next = Q[0]
                
    #             # Add the children, if any, to the back of
    #             # the queue
    #             if node.left:
    #                 Q.append(node.left)
    #             if node.right:
    #                 Q.append(node.right)
        
    #     # Since the tree has now been modified, return the root node
    #     return root
