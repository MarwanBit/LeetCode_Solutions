class Solution:
    def __init__(self):
        '''
        '''
        self.swaps = 0
    
    def graphDFS(self, node: int, connections: list[list[int]], visited: list[bool]) -> None:
        '''
        '''
        visited[node] = True
        for index, edge in enumerate(connections):
            if node in edge and (not visited[edge[0]] or not visited[edge[1]]):
                #If this is true we must swap the edge
                if edge[0] == node:
                    connections[index] = [edge[1], edge[0]]
                    self.swaps += 1 
                if not visited[edge[1]]:
                    self.graphDFS(edge[1], connections, visited)
                if not visited[edge[0]]:
                    self.graphDFS(edge[0], connections, visited)
                
        
    def minReorder(self, n: int, connections: list[list[int]]) -> int:
        '''
        '''
        self.swaps = 0
        visited = [False]*n
        self.graphDFS(0, connections, visited)
        return self.swaps
    

if __name__ == "__main__":
    sol = Solution()
    n_1 = 6
    G_1 = [[0,1],[1,3],[2,3],[4,0],[4,5]]
    n_2 = 5
    G_2 = [[1,0],[1,2],[3,2],[3,4]]
    n_3 = 3 
    G_3 = [[1,0],[2,0]]
    print(sol.minReorder(n_1, G_1))
    print(sol.minReorder(n_2, G_2))
    print(sol.minReorder(n_3, G_3))