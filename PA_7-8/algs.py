# ------------------------------------------------------------------------------------------------------------------------------------------------------
# BFS (PA-7) ===========================================================================================================================================
# ------------------------------------------------------------------------------------------------------------------------------------------------------

# OVERVIEW
#   Closest vertices visited first - "level by level"
#   Begin with any node. Traverse all adjacent nodes, then all nodes adjacent to those 

# data = graph to be searched
# visited = array of booleans; represents which nodes have been visited already
# target = integer (node ID) to look for 
# currentNode = ID of node being searched (integer, not the actual node)
# return value: path from starting point to target value 

def bfs(data, visited, target, currentNode):

    pass

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