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
    LC 112:
    Given the root of a binary tree and an integer targetSum, return true if the tree has a root-to-leaf path such that adding up all the values along the path equals targetSum.
    A leaf is a node with no children.
    '''
    def hasPathSum(self, root: TreeNode, targetSum: int) -> bool:
        def DFS(node, sum):
            if not node.left and not node.right:
                return sum + node.val == targetSum
            
            if not node.left:
                return DFS(node.right, sum + node.val)
            if not node.right:
                return DFS(node.left, sum + node.val)
            else:
                return DFS(node.left, sum + node.val) or DFS(node.right, sum + node.val)
        
        if not root:
            return False
        
        return DFS(root, 0)