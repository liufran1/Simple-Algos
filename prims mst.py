# -*- coding: utf-8 -*-
"""
Created on Thu May 17 08:12:49 2018

@author: franklin
""" 
import time, binheap, sys

infile=""
rawdata=open(infile,"r+")

lines=rawdata.read().split('\n')
rawdata.close()

summary = lines[0].split(' ')
nodes = int(summary[0])

#Preprocess since the file comes in dirty
def preProcess(inputfile):
    jobs = [x.split(' ') for x in inputfile[1:]]

    for item in jobs:
        try:
            item.remove('')
        except ValueError:
            pass
    jobs=list(filter(None,jobs))
    jobs = [[int(entry) for entry in line] for line in jobs]
    return jobs

graph = preProcess(lines)

'''
print("Input Graph: ")
print(graph)
print("\n")
'''
start_time = time.time()
def primNaive(G, numNodes, undirected = True):
    """
    #Function assumes input graph is connected
    #Handle cases where edges are undirected
    #Duplicate edges don't matter because the loop only considers the lowest cost edge
    """    
    if undirected:
        reverseG = [[y,x,c] for [x,y,c] in G]
        G = G + reverseG
    cost = 0
    MST = []
    processed=[1] 
    """#vertices processed so far"""
    """#Outer loop"""
    while len(processed)<numNodes:
        #print("Subtree: ")
        subtree = [x for x in G if x[0] in processed]
        sortedSubtree = sorted(subtree, key=lambda x: x[2], reverse=False)
        #print(sortedSubtree) 
        for edge in sortedSubtree:
            if edge[1] not in processed:
                #print("Adding node: %d \n" %edge[1])
                processed.append(edge[1])
                MST.append(edge)
                cost+=edge[2]
                #print("Current cost: %d" %cost)
                break

    #print("Processed nodes: %d" %len(processed))
    return cost, MST
#print(primNaive(graph,nodes)[1])
print(primNaive(graph,nodes)[0])
print("--- %s seconds to run for naive---" % (time.time() - start_time))

start_time = time.time()

def primBin(G, numNodes, undirected = True):
    toprocess = binheap.BinHeap()
    cost = 0
    MST = []    
    processed=[1]
    mostRecentAdd = 1
    if undirected:
        reverseG = [[y,x,c] for [x,y,c] in G]
        G = G + reverseG   
        """    
    #initialize heap
    #need to reshape graph representation in order to properly apply the heap
    #keeping in mind that dictionary ordering is used in this implementation
    #key is first element, value must be second 
        """
    heapGraph = [[sys.maxsize,x,0] for x in range(1,numNodes+1)]        
    """"""
    toprocess.buildHeap(heapGraph)
    """    
    #vertices processed so far       
    """
    while len(processed)<numNodes:
        """
        #extract min and recompute keys
        #for vertex added, look at all connected vertices and their new keys
    
        #gather all new edges to consider
        """
        #print("Most recent node added: %d" %mostRecentAdd)    
    
        crosses = [[source,dest,cost] for [source,dest,cost] in G if source == mostRecentAdd and dest not in processed]        
        #print("New edges: ")
        #print(crosses)
        """
        #get min cost edges
        #this assumes only one edge between two nodes
        
        #update keys
        #for each node in crosses, delete, update key, reinsert. need to figure out how to delete arbitrary element       
        #this version just rips the tree apart and puts it back together
        """        
        #print("oldHeap: ")
        oldHeap = toprocess.heapList[1:]
        #print(oldHeap)
        graphDict = {node:[weight,source] for [weight,node,source] in oldHeap}
        """"""
        #print("dictionary created")
        for edge in crosses:
            if graphDict[edge[1]][0]>edge[2]:
                '''
                print("Updating edge cost")
                print("Node: %d" %edge[1])
                print("Old cost: %d" %graphDict[edge[1]])
                print("New cost: %d" %edge[2])
                '''
                #graphDict[edge[1]] = edge[2]
                graphDict[edge[1]][0] = edge[2]
                graphDict[edge[1]][1] = edge[0]
        #print("edges updated")
        newHeap = [[weight,node,source] for (node,[weight,source]) in graphDict.items()]
        
        #print("new heaplist created")
        toprocess.buildHeap(newHeap)
        """#get newest edge"""
        addEdge = toprocess.delMin()
        #print("new edge added: ")
        #print(addEdge)
        cost += addEdge[0]
        mostRecentAdd = addEdge[1]
        processed.append(mostRecentAdd)
        sourceNode = addEdge[2] 
        MST.append([sourceNode,mostRecentAdd,addEdge[0]])

    return cost, MST

#print(primBin(graph,nodes)[1])
print(primBin(graph,nodes)[0])
print("--- %s seconds to run for heap implementation---" % (time.time() - start_time))
#way faster even with the inelegant heap key updates