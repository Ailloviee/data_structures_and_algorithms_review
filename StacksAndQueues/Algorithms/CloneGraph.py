# Definition for a Node.
class Node:
    def __init__(self, val=0, neighbors=None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []


# Solution using a stack to implement DFS
class Solution:
    def cloneGraph(self, node: "Node") -> "Node":
        if not node:
            return None

        visited = {}
        stack = [node]
        visited[node] = Node(node.val, [])

        while stack:
            curr_node = stack.pop()
            for neighbor in curr_node.neighbors:
                if neighbor not in visited:
                    visited[neighbor] = Node(neighbor.val, [])
                    stack.append(neighbor)
                visited[curr_node].neighbors.append(visited[neighbor])

        return visited[node]
