# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# Solution using Recursive (Call left, do work, call right)
class Solution:
    '''
    LC 94:
    Given the root of a binary tree, return the inorder traversal of its nodes' values.
    '''
    def inorderTraversal(self, root: TreeNode) -> List[int]:
        l = []

        def traverse(node, lst):
            if not node:
                return 
            traverse(node.left, lst)
            lst.append(node.val)
            traverse(node.right, lst)

        traverse(root, l)

        return l

# Another solution would be using iterative. A stack where you append all left, pop em and do work, then do the node's work, then do right's work
    # def inorderTraversal(self, root: TreeNode) -> List[int]:   
    #     l = []
    #     stack = []
        
    #     cur = root
        
    #     while cur or stack:
    #         while cur:
    #             stack.append(cur)
    #             cur = cur.left
            
    #         cur = stack.pop()
    #         l.append(cur.val)
    #         cur = cur.right
            
    #     return l