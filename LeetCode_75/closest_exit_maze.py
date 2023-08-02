from collections import deque

'''
The problem with this solution is the usage of the adj list which uses alot of extra memory, we can skip
it and check all of the possible directions in one loop
'''

class Solution:
    def graphBFS(self, adjList: dict, entrance: list[int], visited: dict, m, n) -> int:
        '''
        '''
        q = deque()
        q.append([tuple(entrance), 0])
        while q:
            L = len(q)
            for i in range(L):
                curr_node, level = q.popleft()
                visited[curr_node] = True 
                row, col = curr_node 
                if (((row == 0) or (row == m - 1)) or ((col == 0 ) or (col == n - 1))) and curr_node != entrance:
                    return level
                for nei in adjList[curr_node]:
                    if not visited[nei]:
                        q.append([nei, level + 1])
        return -1



    def constructGraph(self, maze:list[list[str]], entrance: list[int]) -> tuple:
        vertices = {}
        adjList = {}
        m = len(maze) #rows
        n = len(maze[0]) #columns
        for row in range(m):
            for col in range(n):
                vertices[(row,col)] = maze[row][col]
        for vertex in vertices:
            adjList[vertex] = []
            row, col = vertex
            if vertices[vertex] != "+":
                neighbors = [ 
                            [row, col + 1],
                            [row, col - 1],
                            [row - 1, col],
                            [row + 1, col]
                            ]
                for nei in neighbors:
                    row, col = nei 
                    if (row in range(m)) and (col in range(n)):
                        if maze[row][col] == ".":
                            adjList[vertex].append((row, col))
        return vertices, adjList, m, n

    def nearestExit(self, maze: list[list[str]], entrance: list[int]) -> int:
        vertices, adjList, m, n = self.constructGraph(maze, entrance)
        entrance = tuple(entrance)
        visited = {vertex: False for vertex in vertices} 
        res = self.graphBFS(adjList, entrance, visited, m, n)
        return res


if __name__ == "__main__":
    sol = Solution()
    maze, entrance = [["+","+",".","+"],[".",".",".","+"],["+","+","+","."]], [1,2]
    maze_2, entrance_2 = [["+","+","+"],[".",".","."],["+","+","+"]], [1,0]
    print(sol.nearestExit(maze, entrance))
    print(sol.nearestExit(maze_2, entrance_2))