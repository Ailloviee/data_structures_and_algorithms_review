from collections import deque 
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# Solution using Recursive (Call left, call right, do work)
class Solution:
    '''
    LC 145:
    Given the root of a binary tree, return the postorder traversal of its nodes' values.
    '''
    def postorderTraversal(self, root: TreeNode) -> List[int]:
        l = []

        def traverse(node, lst):
            if not node:
                return 
            traverse(node.left, lst)
            traverse(node.right, lst)
            lst.append(node.val)

        traverse(root, l)

        return l

# Another solution would be using iterative. A deque where you push left: node, node.right, node.left -> in stack: push node.left first because it gets popped later
    # def postorderTraversal(self, root: TreeNode) -> List[int]:    
    #     if not root:
    #         return []
        
    #     l = deque()
    #     stack = [root]
        
    #     while stack:
    #         node = stack.pop()
            
    #         l.appendleft(node.val)
    #         if node.left:
    #             stack.append(node.left)
    #         if node.right:
    #             stack.append(node.right)

    #     return list(l)