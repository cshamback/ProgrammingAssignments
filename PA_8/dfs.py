from dataStructs import *

def printList(list):
    for i in range(len(list)):
        print(list[i], end=" ")
    print('| ')

def printTB(nodes, colors, prev, first, last):
    print("+" + '-' * (len(nodes)*2 + len("| Predecessors")) + "-+")

    print("| Nodes:        ", end="")
    printList(nodes)
    print("+" + '-' * (len(nodes)*2 + len("| Predecessors")) + "-+")

    print("| Colors:       ", end="")
    printList(colors)
    print("| Predecessors: ", end="")
    printList(prev)
    print("| First Time:   ", end="")
    printList(first)
    print("| Last Time:    ", end="")
    printList(last)

    print("+" + '-' * (len(nodes)*2 + len("| Predecessors")) + "-+")    


def dfs(graph, visited, target, currentNode):

    data = graph
    path = []
    time = 0

    # initialize traceback data
    nodes = []
    colors = [] # w = never, g = at least once, b = all descendants visited
    prev = [] # node visited before this node 
    first = [] # array of times each node was first visited
    last = [] # array of times each node was last visited

    for i in range(len(data)):
        nodes.append(i)
        colors.append('w')
        prev.append('∅')
        first.append('∅')
        last.append('∅')

    printTB(nodes, colors, prev, first, last)

    visited = [False for i in range(len(data))]
    
    # currently visiting a node, so update the visited array
    visited[currentNode] = True

    # base case: found the target -> return it 
    if currentNode == target: 
        return [currentNode] # return path as a list 
    
    # for each node, visit all of its adjacent nodes
    # each node is an array of edges, which are represented by IDs of the node connected by the edge, like this: 
    # 0: [1, 2, 3] -> node 0 has edges connecting to 1, 2, and 3, so we look at the adjacent nodes to all those nodes 
    for node in data:
        if(colors[data.index(node)] == 'w'): # if node has never been visited
            dfsVisit(data, node, visited, colors, prev, first, last, time, target, path) # visit that node

def dfsVisit(data, currentNode, visited, colors, prev, first, last, time, target, path):

    colors[data.index(currentNode)] = 'g'
    first[data.index(currentNode)] = time
    time += 1

    if(target in currentNode):
        return

    for neighbor in currentNode: # iterate through each neighbor connected to the current node  

        if visited[neighbor] == False: # if the current neighbor's node has not been visited, call DFS on it 
            prev[neighbor] = data.index(currentNode)
            dfsVisit(data, data[neighbor], visited, colors, prev, first, last, time, target, path)

    colors[data.index(currentNode)] = 'b'
    last[data.index(currentNode)] = time

    nodes = []
    for i in range(len(data)):
        nodes.append(i)
    printTB(nodes, colors, prev, first, last)

    time += 1
    return


def findersKeepers(graph, beginner_node):
    # A place to store all the nodes we've been to
    # keeps notes
    seen = []
    # keeps track of which nodes to visit next
    stack = [beginner_node]

    # While there's something in the stack, we pop off nodes we've seen
    # Keeps executing until the stack is empty
    while stack:
        node = stack.pop()
        # Checks for nodes we haven't seen and adds to list
        if node not in seen:
            seen.append(node) 
            for next_node in reversed(graph[node]):
                if next_node not in seen:
                    stack.append(next_node)
    return seen

# Returns the adjacency matrix 
def adjacencyMatrix(graph):
    size = len(graph.getGraph())
    matrix = []

    # fills matrix with 0's
    for i in range(size):
        matrix.append([0]*size)

    for beginNode,neighbors in enumerate(graph.getGraph()):
        # Makes connections!
        for endNode in neighbors:
            matrix[beginNode][endNode] = 1 
    return matrix


# Returns adjacency list
def adjacencyList(graph):
    # need to pull the graph from somewhere :)
    graph = graph.getGraph()
    # Somewhere to put empty lists in
    Directory = {}

    # iterate through the graph and key in nodes and their neighbors
    for i, next_node in enumerate(graph):
        Directory[i] = next_node

    # return the list
    return Directory
# Why did the chicken cross the road?
# Test code
"""graph = {
    0: [1, 2],
    1: [0, 3, 4],
    2: [0, 5],
    3: [1],
    4: [1],
    5: [2]
}
DFS(graph, 0)"""

graph = Graph() 
graph.setGraph([[1, 2, 5], [0, 3], [0, 1, 3], [0, 1, 2, 3, 5], [1, 3, 5], [1, 2, 4]])
dfs(graph.getGraph(), [], 5, 0)   

print("Adjacency Matrix: ")
adjacentMatrix = adjacencyMatrix(graph) 
for row in adjacentMatrix:
    print(row)   

print("Adjacency List:")
adjacencyList = adjacencyList(graph)
print(adjacencyList)


toVisit = int(input("Which node do you want to visit? "))
print("Visited Nodes:")
print(findersKeepers(graph.getGraph(),toVisit))