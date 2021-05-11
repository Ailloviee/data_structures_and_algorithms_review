from collections import deque
import math

# Solution using BFS
class Solution:
    def numSquares(self, n):
        """
        :type n: int
        :rtype: int
        """
        edges = [i * i for i in range(1, int(n ** 0.5) + 1)]
        visited = [False] * (n + 1)
        level = 0
        children = [0]
        while True:
            level += 1
            parents = children
            children = []
            for parent in parents:
                for edge in edges:
                    child = parent + edge
                    if child == n:
                        return level
                    if child > n:
                        break
                    if visited[child]:
                        continue
                    visited[child] = True
                    children.append(child)
