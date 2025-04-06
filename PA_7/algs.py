from dataStructs import *

# ------------------------------------------------------------------------------------------------------------------------------------------------------
# BFS (PA-7) ===========================================================================================================================================
# ------------------------------------------------------------------------------------------------------------------------------------------------------

# OVERVIEW
#   Closest vertices visited first - "level by level"
#   Begin with any node. Traverse all adjacent nodes, then all nodes adjacent to those 

def printList(list):
    for i in range(len(list)):
        print(list[i], end=" ")
    print('| ')

def printTB(nodes, colors, distances, prev):
    print("+" + '-' * (len(nodes)*2 + len("| Distances")) + "-+")

    print("| Nodes:     ", end="")
    printList(nodes)
    print("+" + '-' * (len(nodes)*2 + len("| Distances")) + "-+")

    print("| Colors:    ", end="")
    printList(colors)
    print("| Distances: ", end="")
    printList(distances)
    print("| Prev:      ", end="")
    printList(prev)

    print("+" + '-' * (len(nodes)*2 + len("| Distances")) + "-+")  

def bfs(s, e, data): # s = start node, e = end node, data = graph represented as 2d array 

    # before doing anything, print initial tb chart
    # initialize new traceback data
    colors = ['w' for _ in data]
    distances = ['∞' for _ in data]
    prevTb = ['∅' for node in data] # path from start to end is empty 

    nodes = []
    for i in range(len(data)):
        nodes.append(i)

    printTB(nodes, colors, distances, prevTb)

    # broken up BFS into two smaller methods for simplicity  
    prev = [None for node in data]
    prev = solve(s, data)
    return reconstructPath(s, e, prev)

def solve(s, data): # most of the work for BFS done here

    # initialize new traceback data
    colors = ['w' for _ in data]
    distances = ['∞' for _ in data]
    prevTb = ['∅' for node in data]

    # initialize head
    colors[s] = 'g'
    distances[s] = 0

    nodes = []
    for i in range(len(data)):
        nodes.append(i)
    
    q = Queue() # create a new, empty queue
    q.enqueue(s) # add start node to queue 
    
    prev = [None for node in data] # path from start to end is empty 

    visited = [False for node in data] # one value of false (not visited) for each node in the graph
    visited[s] = True # but we did visit the start node
    
    while(len(q.getList()) > 0): # while queue is not empty 
        node = q.dequeue()
        
        neighbors = data[node] # data[node] returns a list of neighbors that node has 

        # node is the node we're currently visiting
        # next is the neighbor of node we're currently looking at 
        
        for next in neighbors: 
            
            if not visited[next]: # loop over all unvisited nodes
                # update traceback table - since nodes are ints, we can just use them as indices
                colors[next] = 'g' # node is being visited for the first time - make it gray
                distances[next] = distances[node] + 1

                if(node == None):
                    prevTb[next] = '∅'
                else:
                    prevTb[next] = node
                
                q.enqueue(next) # find a next unvisited node 
                
                visited[next] = True # mark node as visited 
                
                prev[next] = node # add parent of next node to prev array - "to get to next, we came from node"

                # result example: prev = [None, 0, 1, None, 2] => path looks like this: [start, 1, 2, 4]
        colors[node] = 'b'
        printTB(nodes, colors, distances, prevTb)
        print(f" WOW: {q.getList()}")
        

    return prev # return path we just built 

def reconstructPath(s, e, prev): # ensures path is a valid path from S -> E and returns that path 
    # reconstruct path backwards from e to s
    path = []
    #print(f"Reconstructing path from {s} to {e}")

    # iterate through prev array from e to s
    # stop if we find a null value 
    curr = e 
    while curr is not None: 
        path.append(curr)
        curr = prev[curr]

    path.reverse()

    # check if path actually starts at s, 
    # therefore s and e are connected in the graph 
    if len(path) > 0 and path[0] == s:
        return path

    # if s and e are not connected, return nothing 
    return []

# ------------------------------------------------------------------------------------------------------------------------------------------------------
# DFS (PA-8) ===========================================================================================================================================
# ------------------------------------------------------------------------------------------------------------------------------------------------------

# OVERVIEW
#   traverse all adjavent vertices
#   each time we visit a vertex, we completely finish the traversal of all its adjacent vertices
#   graphs (unlike trees) contain cycles -> use boolean visited array to combat this 

# every recursive call of DFS searches a new node in the graph 

def dfs(data, visited, target, currentNode):

    # currently visiting a node, so update the visited array
    visited[currentNode] = True

    # base case: found the target -> return it 
    if currentNode == target: 
        return [currentNode] # return path as a list 
    
    # for each node, visit all of its adjacent nodes
    # each node is an array of edges, which are represented by IDs of the node connected by the edge, like this: 
    # 0: [1, 2, 3] -> node 0 has edges connecting to 1, 2, and 3, so we look at the adjacent nodes to all those nodes 

    for neighbor in data[currentNode]: # iterate through each neighbor connected to the current node  

        if visited[neighbor] == False: # if the current neighbor's node has not been visited, call DFS on it 

            path = dfs(data, visited, target, neighbor) # pass the whole list recursively but change the current node as an integer index
            if path:
                return [currentNode] + path
            
def adjacencyMatrix(graph):
    size = len(graph)
    matrix = []

    # fills matrix with 0's
    for i in range(size):
        matrix.append([0]*size)

    for beginNode,neighbors in enumerate(graph):
        # Makes connections!
        for endNode in neighbors:
            matrix[beginNode][endNode] = 1 
    return matrix


