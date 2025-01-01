from algs import * 
from graph import * 

graph = Graph()

# HELPER FUNCTIONS

# converts string of ints separated by commas to array of ints, with error checking 
def getArray(input):

    # if input is q or Q, it means we've reached the end of the inputs -> q/Q is not trying to be a node, so don't try to turn it into one
    if input == "q" or input == "Q":
        return None
    
    result = input.split(",") # creates list where every item is what the user separated by commas, but each of these is a string 

    # attempt to convert each item from string to int 
    try:
        resultInt = [int(x) for x in result]
    except ValueError: 
        print("Invalid input. One or more edges in , ", input, " is not an integer. Disregarding this node.")
        return None

    return resultInt 

# ------------------------------------------------------------------------------------------------------------------------------------------------------
# GET GRAPH FROM USER ==================================================================================================================================
# ------------------------------------------------------------------------------------------------------------------------------------------------------

print("Enter nodes one at a time.")
print("Each should be a series of integers separated by commas. Press enter between nodes.")
print("Nodes will be named automatically, with numbers starting from 0 in ascending order.")
print("Any nodes that were not created but have edges connected to them will also be added automatically.")
print("Press Q to finish.")
nextInput = "" # declare input outside while loop but don't get a value yet 

while(nextInput != "q" and nextInput != "Q"):
    nextInput = input()

    vertex = getArray(nextInput)

    if vertex != None: #getArray returns none if input is invalid. if it is invalid, don't create anything. 
        graph.addVertex(vertex)

# add extra nodes: user can specify edges that were not added as nodes:
#   ie. have nodes named 0 and 1 that connect to a 4 and a 5, but never actually created 4 and 5.
#   we need to make these nodes exist, as well as a node 2 and 3 that have no edges since none were specified 

graphArr = graph.getGraph()
for currNode in range(0, len(graphArr)): # look at every node 
    for currEdge in range(0, len(graphArr[currNode])): # look at every edge in that node 

        value = graphArr[currNode][currEdge]

        # every node's "name" corresponds to its index in the graph 2D array. 
        # therefore, if the current edge is a number >= the number of rows in graph, we need to add that node at the correct position as well as any missing nodes before it. 
        if(value >= len(graphArr)): 

            # add (value - len(graph) + 1) empty nodes to array
            for i in range(value - len(graphArr) + 1):
                graph.addVertex([])

            # give the newly added node an edge pointing to the node where it was found 
            # addEdge() automatically prevents duplicate edges 
            graph.addEdge(currNode, value)

print("Your graph so far:")
graph.printGraph()

nextInput = input("Would you like to add any additional edges before moving on to the SCC algorithm? (Y/N)")

if(nextInput == "Y" or nextInput == "y"):
    print("Please enter your additional edges as sets of two integers (the nodes with that edge) separated by a comma. Press Q when finished.")
    while(nextInput != "q" and nextInput != "Q"):
        nextInput = input()

        edges = getArray(nextInput)
        if edges != None:  #getArray returns none if input is invalid. if it is invalid, don't create anything. 
            graph.addEdge(edges[0], edges[1])

print("Your finished graph: ")
graph.printGraph()

# ------------------------------------------------------------------------------------------------------------------------------------------------------
# RUN SCC ==============================================================================================================================================
# ------------------------------------------------------------------------------------------------------------------------------------------------------

# ------------------------------------------------------------------------------------------------------------------------------------------------------
# OUTPUT ALL SCC SUBGRAPHS =============================================================================================================================
# ------------------------------------------------------------------------------------------------------------------------------------------------------