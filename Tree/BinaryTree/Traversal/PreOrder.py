# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# Solution using Recursive (Do work, call left, call right)
class Solution:
    '''
    LC 144:
    Given the root of a binary tree, return the preorder traversal of its nodes' values.
    '''
    def preorderTraversal(self, root: TreeNode) -> List[int]:
        l = []
       
        def traverse(node, lst):
            if not node:
                return 
            lst.append(node.val)
            traverse(node.left, lst)
            traverse(node.right, lst)
        
        traverse(root, l)
        
        return l
        
# Another solution would be using iterative. A stack where you do work, append the right node then left node (So left gets popped first)
    # def preorderTraversal(self, root: TreeNode) -> List[int]:
    #     if not root:
    #         return []
    #     l = []
    #     stack = [root]
        
    #     while stack:
    #         node = stack.pop()
            
    #         l.append(node.val)
    #         if node.right:
    #             stack.append(node.right)
    #         if node.left:
    #             stack.append(node.left)
    #     return l