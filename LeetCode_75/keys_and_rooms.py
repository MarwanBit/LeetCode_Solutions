from typing import Optional

class Solution:
    def graphDFS(self, node: int, rooms:list[list[int]], visited: list[bool]) -> None:
        '''
        '''
        visited[node] = True
        neighbors = rooms[node]
        for v in neighbors:
            if not visited[v]:
                self.graphDFS(v, rooms, visited)

    def canVisitAllRooms(self, rooms: list[list[int]]) -> bool:
        '''
        '''
        n = len(rooms)
        visited = [False]*n 
        self.graphDFS(0, rooms, visited)
        return visited == [True]*n


if __name__ == "__main__":
    sol = Solution()
    rooms_1 = [[1], [2], [3], []]
    rooms_2 = [[1,3], [3, 0, 1], [2], [0]]
    print(sol.canVisitAllRooms(rooms_1))
    print(sol.canVisitAllRooms(rooms_2))
