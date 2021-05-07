from collections import deque
DIRECTIONS = [(-1, 0), (1, 0), (0, -1), (0, 1)]

# Solution using a deque to implement a queue that does BFS starting from the Gates
class Solution:
    '''
    LC 286
    '''
    def wallsAndGates(self, rooms: List[List[int]]) -> None:
        """
        Do not return anything, modify rooms in-place instead.
        """
        Q = deque()
        m, n = len(rooms), len(rooms[0])
        for i in range(m):
            for j in range(n):
                if rooms[i][j] == 0:
                    Q.append((i, j))
        
        while Q:
            i, j = Q.popleft()
            for direction in DIRECTIONS:
                r = i + direction[0]
                c = j + direction[1]
                
                if r < 0 or c < 0 or r >= m or c >= n or rooms[r][c] <= rooms[i][j] + 1:
                    continue
                
                rooms[r][c] = rooms[i][j] + 1
                Q.append((r,c))