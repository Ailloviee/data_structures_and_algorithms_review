from collections import deque
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# Solution using recursive
class Solution:
    '''
    LC 101:
    Given the root of a binary tree, check whether it is a mirror of itself (i.e., symmetric around its center).
    '''
    def isSymmetric(self, root: TreeNode) -> bool: 
        def isMirror(t1, t2):
            if not t1 and not t2: return True
            if not t1 or not t2: return False
            
            return t1.val == t2.val and isMirror(t1.left, t2.right) and isMirror(t1.right, t2.left)
        
        return isMirror(root, root)