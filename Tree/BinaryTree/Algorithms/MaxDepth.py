from collections import deque
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# Solution using recursive, at each node, depth is the maximum depth of current + depth of left and current + depth of right
class Solution:
    '''
    LC 104:
    Given the root of a binary tree, return its maximum depth.
    A binary tree's maximum depth is the number of nodes along the longest path from the root node down to the farthest leaf node.
    '''
    def maxDepth(self, root: TreeNode) -> int:
        def dfs(node, d):
            if not node:
                return d
            else:
                return max(dfs(node.left, d+1), dfs(node.right, d+1))
            
        
        return dfs(root, 0)