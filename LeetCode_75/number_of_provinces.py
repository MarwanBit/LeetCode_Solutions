class Solution:
    def processAdjList(self, adjRow: list[int]) -> list[int]:
        '''
        We take the row A_{i} of our adjacency list and return a list of 
        '''
        adjList = []
        for index in adjRow:
            if index == 1:
                adjList.append(index)
        return adjList 

    def graphDFS(self, node: int, isConnected, visited: list[bool]) -> None:
        '''
        '''
        visited[node] = True 
        for index in self.processAdjList(isConnected[node]):
            if not visited[index]:
                self.graphDFS(index, isConnected, visited)
    
    def findCircleNum(self, isConnected: list[list[int]]) -> int:
        '''
        The approach for this problem is we are going to count the number
        of connected components in the graph, we are given the adjacency list
        so what we will do is choose some random vertex 1, ..., n and do DFS on 
        that vertex, marking the visited nodes. once it is finished this means we 
        have visited one connected component, we keep continuing until we've visited
        all of them
        '''
        num_connected_components = 0 
        visited = [False]*len(isConnected)
        n = len(isConnected)
        while visited != [True]*len(isConnected):
            for index in range(n):
                if not visited[index]:
                    self.graphDFS(index, isConnected, visited)
                    num_connected_components += 1 
        return num_connected_components



if __name__ == "__main__":
    sol = Solution()
    graph_1 = [[1,1,0],[1,1,0],[0,0,1]]
    graph_2 = [[1,0,0],[0,1,0],[0,0,1]]
    graph_3 = [[1]]
    #Notice that graph_1[i] gives the "adjanency list" for the vertex i, what we need to do is convert this into a list 
    # of indices, 
    print(sol.findCircleNum(graph_1))
    print(sol.findCircleNum(graph_2))
    print(sol.findCircleNum(graph_3))
        