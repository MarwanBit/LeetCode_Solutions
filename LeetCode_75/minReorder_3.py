class Solution:
    def __init__(self):
        '''
        '''
        self.swaps = 0
    
    def graphDFS(self, node: int, edges: dict, neighbors: dict, visited: list[bool]) -> None:
        '''
        '''
        visited[node] = True
        for neighbor in neighbors[node]:
            if (neighbor, node) not in edges and not visited[neighbor]:
                self.swaps += 1 
            if not visited[neighbor]:
                self.graphDFS(neighbor, edges, neighbors, visited)
                
        
    def minReorder(self, n: int, connections: list[list[int]]) -> int:
        '''
        '''
        self.swaps = 0
        visited = [False]*n
        #This works theoretically but we should use and adjacency list
        edges = {(a,b) for a,b in connections}
        neighbors = {city: [] for city in range(n)}
        for edge in edges:
            a, b = edge
            neighbors[a].append(b)
            neighbors[b].append(a)
        self.graphDFS(0, edges, neighbors, visited)
        return self.swaps