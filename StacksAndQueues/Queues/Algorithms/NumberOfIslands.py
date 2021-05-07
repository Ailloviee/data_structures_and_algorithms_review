# Solution using a list to implement a stack that does DFS
class Solution:
    '''
    LC 200
    '''
    def numIslands(self, grid: List[List[str]]) -> int:
        def DFS(q, grid, m, n):
            while len(q) != 0:
                i, j = q.pop()
                if i-1 >= 0 and grid[i-1][j] == '1':
                    grid[i-1][j] = '0'
                    q.append((i-1, j))
                if i + 1 < m and grid[i+1][j] == '1':
                    grid[i+1][j] = '0'
                    q.append((i+1, j))
                if j-1 >= 0 and grid[i][j-1] == '1':
                    grid[i][j-1] = '0'
                    q.append((i, j-1))
                if j+1 < n and grid[i][j+1] == '1':
                    grid[i][j+1] = '0'
                    q.append((i, j+1))
                
        
        m, n = len(grid), len(grid[0])
        res = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == '1':
                    res += 1
                    q = [(i,j)]
                    DFS(q, grid, m, n)
        
        return res