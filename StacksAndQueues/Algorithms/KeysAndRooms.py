# Solution using BFS
class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        N = len(rooms)

        visited = [False for _ in range(N)]
        visited[0] = True

        Q = [0]

        while Q:
            curr = Q.pop()
            for key in rooms[curr]:
                if not visited[key]:
                    visited[key] = True
                    Q.append(key)

        return sum(visited) == N
