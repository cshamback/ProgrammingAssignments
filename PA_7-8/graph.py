# IMPLEMENTATION OF AN UNDIRECTED GRAPH DATA STRUCTURE 

# each graph object is a 2D array: 
#   the index of a row is the name of the node 
#   the contents of the rows are nodes that connect to it (edges)

class Graph: 

    # each instance of Graph has a 2D array called graph
    def __init__(self):
        self.graph = []

    # adding an edge between a and b (integers, each representing a node)
    # direction a -> b (row a has edge b)
    def addEdge(self, a, b):
        # prevent duplicate edges by checking first if the edge is already there 
        if not (b in self.graph[a]):
            self.graph[a].append(b)
        if not (a in self.graph[b]):
            self.graph[b].append(a)

    # add a new row to the table
    # a vertex is an array of edges that connect to the vertex
    # vertex number/name is automatically assigned 
    def addVertex(self, vertex):
        self.graph.append(vertex)

    def printGraph(self):
        # for every node, print the name of the node and the names of all its connections
        # ie. 0: [1 2 3 4]
        for i in range(len(self.graph)):
            print(i, ": ", [item for item in self.graph[i]])

    def getGraph(self):
        return self.graph
    
    # testing purposes only 
    # allows us to avoid the UI loops 
    def setGraph(self, graphVals):
        self.graph = graphVals
