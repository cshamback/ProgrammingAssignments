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


# This is Cody's code on DFS. Putting it here so I can merge with my version later.
# Thank you Cody.
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

# Liem's code
# I FOUND IT  
def DFS(graph, beginner_node):

    # A place to store all the nodes we've seen
    seen = []
    seen.append(beginner_node)

    stack = [beginner_node]

    # While there's something in the stack, we pop off nodes
    # Keeps executing until the stack is empty
    while stack:
        node = stack.pop()
        for next_node in graph[node]:
            # Checks for nodes we haven't seen
            if next_node not in seen:
                #Visit this node
                seen.append(next_node)
                # Put this in the stack
                stack.append(next_node)
        print(node)

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

<<<<<<< HEAD
graph = Graph() 
graph.setGraph([[1, 2, 5], [0, 3], [0, 1, 3], [0, 1, 2, 3, 5], [1, 3, 5], [1, 2, 4]])
dfs(graph.getGraph(), [], 5, 0)       
=======
# dfs part of pa-7
# ------------------------------------------------------------------------------------------------------------------------------------------------------
# RUN DFS ==============================================================================================================================================
# ------------------------------------------------------------------------------------------------------------------------------------------------------

#dfs(graph, target, startingNode) -> can start at any node, arbitrarily choosing 0
# start node specified by the user 

# DFS stuff 
"""# one index for each node in graph, all start as False because no one has been visited yet 
# declare this array outside the DFS() method because dfs is recursive. this avoids the visited array being reset every run, causing overflow 
visited = [False for i in range(len(graph.getGraph()))]
print("Result: ", dfs(graph.getGraph(), visited, e, s), "\n")"""


# test data
"""nodes = [1, 2, 3, 4, 5, 6]
colors = ['w', 'g', 'b', 'b', 'b', 'b']
distances = [0, 4, 5, 1, 0, 2]
prev = [1, 4, 5, 3, 4, 1]

printTB(nodes, colors, distances, prev)"""

# ------------------------------------------------------------------------------------------------------------------------------------------------------
# OUTPUT RESULTS (DFS) =================================================================================================================================
# ------------------------------------------------------------------------------------------------------------------------------------------------------
>>>>>>> 7ec2d78a30b8aa4cc0a66054b1452426056432f4
