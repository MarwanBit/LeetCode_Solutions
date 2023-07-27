class Solution:
    def relevantEdges(self, node: int, connections:list[list[int]]) -> list[list[int]]:
        '''
        '''
        return [x for x in enumerate(connections) if node in x[1]]
    
    def graphDFS(self, node: int, connections: list[list[int]], visited: list[bool], swaps: int) -> None:
        '''
        '''
        relevant_edges = self.relevantEdges(node, connections)
        visited[node] = True
        print("Current Node: ", node)
        print("relevant Edges: ", relevant_edges)
        for index, edge in relevant_edges:
            print("current Edge: ", edge)
            print("current index: ", index)
            if node == edge[0] and not visited[edge[1]]:
                print("Swap being done!")
                connections[index] = [edge[1], node]
                print("Connections after swap!", connections)
                swaps += 1 
                self.graphDFS(edge[1], connections, visited, swaps)
            
        
    def minReorder(self, n: int, connections: list[list[int]]) -> int:
        '''
        '''
        swaps = 0
        visited = [False]*n
        self.graphDFS(0, connections, visited, swaps)
        print(connections)
        return swaps


if __name__ == "__main__":
    sol = Solution()
    n_1 = 6
    G_1 = [[0,1],[1,3],[2,3],[4,0],[4,5]]
    n_2 = 5
    G_2 = [[1,0],[1,2],[3,2],[3,4]]
    n_3 = 3 
    G_3 = [[1,0],[2,0]]
    print(sol.minReorder(n_1, G_1))