# Solution using BFS
class Solution:
    def floodFill(
        self, image: List[List[int]], sr: int, sc: int, newColor: int
    ) -> List[List[int]]:
        DIRECTIONS = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        m, n = len(image), len(image[0])
        oldValue = image[sr][sc]

        visited = set()
        visited.add((sr, sc))

        Q = [(sr, sc)]

        while Q:
            r, c = Q.pop()
            image[r][c] = newColor

            for d in DIRECTIONS:
                nr = r + d[0]
                nc = c + d[1]
                if (
                    0 <= nr < m
                    and 0 <= nc < n
                    and (nr, nc) not in visited
                    and image[nr][nc] == oldValue
                ):
                    visited.add((nr, nc))
                    Q.append((nr, nc))

        return image
