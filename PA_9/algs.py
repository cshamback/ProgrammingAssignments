from dataStructs import * 

# IMPLEMENTATION OF SCC ALGORITHM
# returns array of Graph objects, each representing a sub-graph

# Translated from pseudocode 
def scc(graph):
    index = [0]
    indices = {}
    stack = Stack()
    occupied_stack = set()
    lowlinks = {}
    result = [] 
    def connect(vertex):
        indices[vertex] = index[0]
        lowlinks[vertex] = index[0]
        index[0] += 1

        stack.push(vertex)
        occupied_stack.add(vertex)

        for nextVertex in graph[vertex]:
            if nextVertex not in indices:
                connect(nextVertex)
                lowlinks[vertex] = min(lowlinks[vertex],lowlinks[nextVertex])
            elif nextVertex in occupied_stack:
                lowlinks[vertex] = min(lowlinks[vertex], indices[nextVertex])

        if lowlinks[vertex] == indices[vertex]:
            connectedComponent = []
            while True:
                y = stack.pop()
                occupied_stack.remove(y)
                connectedComponent.append(y)

                if y == vertex:
                    break

            result.append(connectedComponent)

    for v in range(len(graph)):
        if v not in indices:
            connect(v)


# OVERVIEW - DEPTH-FIRST SEARCH (DFS)
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
            
# Testing if we can do something here
def DFSL(graph, beginner_node):

    # A place to store all the nodes we've seen
    seen = []
    stack = [beginner_node]
    seen.append(beginner_node)

    # While there's something in the stack, we pop off nodes
    # Keeps executing until the stack is empty
    while stack:
        node = stack.pop()
        for next_node in graph[node]:
            # Checks for nodes we haven't seen
            for neighbor in graph[node]:
                if neighbor not in seen:
                    seen.append(neighbor) # Mark neighbor as seen.
                    stack.append(neighbor)
    print(seen)