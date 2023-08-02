from collections import deque

class Solution:
    def constructGraph(self, grid: list[list[int]]) -> tuple:
        vertices = {}
        m = len(grid) #rows
        n = len(grid[0]) #columns
        for row in range(m):
            for col in range(n):
                vertices[(row, col)] = grid[row][col]
        return vertices, m, n

    def BFS(self, start_node, vertices, visited, m, n):
        visited[start_node] = True
        if vertices[start_node] == 2:
            vr, vq, rot = start_node[0], start_node[1], vertices[start_node]
            for dr, dq in [[1,0], [-1, 0], [0,1], [0, -1]]:
                nr, nq = vr + dr, vq + dq
                if (0 <= nr < m) and (0 <= nq < n) and not visited[(nr, nq)]:
                    if vertices[(nr,nq)] == 1:
                        vertices[(nr,nq)] = 2
                        visited[start_node] = True


    def orangesRotting(self, grid: list[list[int]]) -> int:
        vertices, m, n = self.constructGraph(grid)
        visited = {vertex: False for vertex in vertices}
        min_count = 0
        while (1 in vertices.values()) or (False in visited):
            for vertex in vertices:
                self.BFS(vertex, vertices, visited, m, n)
            min_count += 1
        return min_count

