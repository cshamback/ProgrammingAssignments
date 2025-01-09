from dataStructs import *

# ------------------------------------------------------------------------------------------------------------------------------------------------------
# BFS (PA-7) ===========================================================================================================================================
# ------------------------------------------------------------------------------------------------------------------------------------------------------

# OVERVIEW
#   Closest vertices visited first - "level by level"
#   Begin with any node. Traverse all adjacent nodes, then all nodes adjacent to those 

def bfs(s, e, data): # s = start node, e = end node, data = graph represented as 2d array 
    # broken up BFS into two smaller methods for simplicity  
    prev = solve(s, data)
    return reconstructPath(s, e, prev)

def solve(s, data): # most of the work for BFS done here
    q = Queue() # create a new, empty queue
    q.enqueue(s) # add start node to queue 

    visited = [False for node in data] # one value of false (not visited) for each node in the graph
    visited[s] = True # but we did visit the start node

    prev = [None for node in data] # path from start to end is empty 

    while(len(q.getList()) > 0): # while queue is not empty 
        node = q.dequeue()
        neighbors = data[node] # data[node] returns a list of neighbors that node has 

        # node is the node we're currently visiting
        # next is the neighbor of node we're currently looking at 
        
        for next in neighbors: 
            if not visited[next]: # loop over all unvisited nodes 
                q.enqueue(next) # find a next unvisited node 

                visited[next] = True # mark node as visited 
                prev[next] = node # add parent of next node to prev array - "to get to next, we came from node"

                # result example: prev = [None, 0, 1, None, 2] => path looks like this: [start, 1, 2, 4]

    return prev # return path we just built 

def reconstructPath(s, e, prev): # ensures path is a valid path from S -> E and returns that path 
    # reconstruct path backwards from e to s
    path = []

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