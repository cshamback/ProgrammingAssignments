# IMPLEMENTATION OF A DIRECTED GRAPH DATA STRUCTURE AND A STACK

# each graph object is a 2D array: 
#    the index of a row is the name of the node 
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

class Stack:
    # implements stack as an array with three built in methods: Push, Peek and Pop. 
    def __init__(self):
        self.stack = []

    # put the parameter in the front position of the array 
    def push(self, value):
        self.stack.insert(0, value) # insert some integer, value, at index 0

    # return the first item in the stack but don't change anything 
    def peek(self):
        return self.stack[0]

    # remove the first item from the stack and return its value 
    def pop(self):
        value = self.stack[0] # store top element as value (not array)
        self.stack.remove(self.stack[0]) # remove finds elements by value not index, so we have to get the value at 0 in order to remove it 
        return value
    
    # return stack as a list
    def getStack(self):
        return self.stack 
