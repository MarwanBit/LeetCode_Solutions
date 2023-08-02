class Solution:
    def constructGraph(self, equations: list[list[str]], values: list[float]) -> list[set, dict]: 
        '''
        Constructr graph takes our list of equations alongside values and returns a list of the form
        [vertices: set, adjList: dict]
        '''
        #This initializes the set of vertices
        vertices = set()
        for equation in equations:
            A_i, B_i = equation 
            if A_i not in vertices: vertices.add(A_i)
            if B_i not in vertices: vertices.add(B_i)
        #Now we will construct the adjacency list 
        adjList = {vertex: [] for vertex in vertices}
        for index, equation in enumerate(equations):
            A_i, B_i = equation
            adjList[A_i].append([B_i, values[index]])
            adjList[B_i].append([A_i, (1/values[index])])
        return [vertices, adjList]
    
    def graphDFS(self, start_node: str, goal_node: str, prev_weights: int, adjList: dict[str: list], visited: dict, vertices) -> int:
        '''
        '''
        visited[start_node] = True 
        #If we find the desired 
        if start_node not in vertices or goal_node not in vertices:
            return - 1
        if start_node == goal_node:
                return prev_weights 
        for (neighbor, weight) in adjList[start_node]:
            if not visited[neighbor]:
                # Do something additionally
                x = self.graphDFS(neighbor, goal_node, prev_weights * weight,  adjList, visited, vertices)
                if x == -1:
                    continue
                else:
                    return x
        return -1
                #Must do something additionally on the valeu of the weights i naddition to if we reach our goal node

    def calcEquation(self, equations: list[list[str]], values: list[float], queries: list[list[str]]) -> list[float]:
        '''
        Notice here that we are constructing a directed graph where each of the 
        A_i's and B_i's are out nodes in the graph and the edges connect (a_i, b_i)
        with a value v_i, so it is directed (we will have 2 edges per connection).

        The idea is to do the following.....

        Construct the graph by iterating through the equations and creating nodes
        for each of the A_i's and B_i's, with the directed weights v_i.

        When evaluating any of the queries C_i / D_i perform DFS or BFS on C_i or 
        D_i to find a path 
            - if no path exists return -1 
            - if a path exists we get a value so it will be 1/ g or g/1 where g 
            is the value we get by following the path and multiplying the weights
            in that given order 
            - return the given value!

        Ideas for traversal: use a stack in addition to recursive DFS To keep track of the current list of 
        values, the key idea behind this problem is that we must be able to find a path from C_i to D_i,
        and we must take the product of the values as we do so. O
        '''
        #This initializes the set of vertices
        vertices, adjList = self.constructGraph(equations, values)
        visited = {vertex: False for vertex in vertices}
        res = []
        for query in queries:
            c_i, d_i = query
            res.append(self.graphDFS(c_i, d_i, 1, adjList, visited, vertices))
            visited = {vertex: False for vertex in vertices}
        return res

