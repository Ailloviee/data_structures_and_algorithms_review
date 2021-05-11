from collections import deque

# Solution using BFS
class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        m, n = len(mat), len(mat[0])
        res = [[float("inf") for _ in range(n)] for _ in range(m)]

        Q = deque()
        DIRECTIONS = [(0, 1), (0, -1), (1, 0), (-1, 0)]

        for i in range(m):
            for j in range(n):
                if mat[i][j] == 0:
                    Q.append((i, j))
                    res[i][j] = 0

        while Q:
            x, y = Q.popleft()

            for d in DIRECTIONS:
                nx, ny = x + d[0], y + d[1]

                if 0 <= nx < m and 0 <= ny < n and res[nx][ny] > 1 + res[x][y]:
                    res[nx][ny] = 1 + res[x][y]
                    Q.append((nx, ny))

        return res

