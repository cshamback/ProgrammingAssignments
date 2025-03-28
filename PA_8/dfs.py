from dataStructs import *

# This is Cody's code on DFS. Putting it here so I can merge with my version later.
# Thank you Cody.
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


# Liem's code
# I FOUND IT  
def DFS(graph, beginner_node):
    # Start at this node
    beginner_node = 0

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
graph = {
    0: [1, 2],
    1: [0, 3, 4],
    2: [0, 5],
    3: [1],
    4: [1],
    5: [2]
}
DFS(graph, 0)
        

