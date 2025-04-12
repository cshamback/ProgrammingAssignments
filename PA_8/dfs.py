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
    data = graph.getGraph()
    time = [0]  # <-- wrapped in list so it can be updated across recursive calls
    path = []

    # initialize traceback data
    nodes = list(range(len(data)))
    colors = ['w'] * len(data)
    prev = ['∅'] * len(data)
    first = ['∅'] * len(data)
    last = ['∅'] * len(data)

    # initial tracking table
    printTB(nodes, colors, prev, first, last)

    visited = [False for _ in range(len(data))]

    dfsVisit(data, currentNode, visited, colors, prev, first, last, time, target, path)


def dfsVisit(data, currentNode, visited, colors, prev, first, last, time, target, path):
    visited[currentNode] = True
    colors[currentNode] = 'g'
    first[currentNode] = time[0]
    time[0] += 1

    if currentNode == target:
        return

    for neighbor in data[currentNode]:  # now we loop over neighbors correctly
        if not visited[neighbor]:
            prev[neighbor] = currentNode
            dfsVisit(data, neighbor, visited, colors, prev, first, last, time, target, path)

    colors[currentNode] = 'b'
    last[currentNode] = time[0]
    time[0] += 1

    # show updated table
    nodes = list(range(len(data)))
    printTB(nodes, colors, prev, first, last)



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
def adjacencyMatrix(graphList):
    size = len(graphList)
    matrix = []

    # fills matrix with 0's
    for i in range(size):
        matrix.append([0]*size)

    for beginNode,neighbors in enumerate(graphList):
        # Makes connections!
        for endNode in neighbors:
            matrix[beginNode][endNode] = 1 
    return matrix


# Returns adjacency list
def adjacencyList(graphList):
    # Somewhere to put empty lists in
    Directory = {}

    # iterate through the graph and key in nodes and their neighbors
    for i, next_node in enumerate(graphList):
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

#graph = Graph() 
#graph.setGraph([[1, 2, 5], [0, 3], [0, 1, 3], [0, 1, 2, 3, 5], [1, 3, 5], [1, 2, 4]])

#dfs(graph.getGraph(), [], 5, 0)  

# DFS stuff 
"""# one index for each node in graph, all start as False because no one has been visited yet 
# declare this array outside the DFS() method because dfs is recursive. this avoids the visited array being reset every run, causing overflow 
visited = [False for i in range(len(graph.getGraph()))]
print("Result: ", dfs(graph.getGraph(), visited, e, s), "\n")"""

#dfs(graph.getGraph(), [], 5, 0)   