#find faster implementation of graph contraction without creating new graph every time. UnionFind data structure?
import math, time, random
start_time = time.time()
#takes as input adjacency list graph representation with list elements tab-separated and lists newline-separated
infile="" 
raw_data=open(infile,"r+")
intlist=raw_data1.read().split('\n')
raw_data.close()

try:
    intlist.remove('')
except ValueError:
    pass
intlist=[x.split('\t') for x in intlist]
print(intlist)
for i in range(len(intlist)):
    try:
        intlist[i].remove('')
    except ValueError:
        pass
    x=[int(j) for j in intlist[i]]
    intlist[i]=x
    intlist[i][0]=[x[0]]

def mergeEdge(num1,num2):
    index=num1[0]+num2[0]
    temp1=[x for x in num1[1:] if x not in index]
    temp2=[x for x in num2[1:] if x not in index]
    return [index]+temp1+temp2
    
def kargerMinCut(adjlist1,iters):

    mincut=10000
    minconfig=[]
    i=0
    while i<iters:
        print(i)
        adjlist2=[x for x in adjlist1]
        while len(adjlist2)>2:
            first=random.randint(0,len(adjlist2)-1)
            second=secondVertex(adjlist2[first],adjlist2)
            temp=mergeEdge(adjlist2[first],adjlist2[second])
            try:
                if first>second:
                    del adjlist2[first]
                    del adjlist2[second]
                else:
                    del adjlist2[second]
                    del adjlist2[first]
            except IndexError:
                print("Index Error")
                print(adjlist2)
                print(first)
                print(second)
                break
            adjlist2=adjlist2+[temp]
            
        if mincut>max([len(x) for x in adjlist2])-1:
            mincut=max([len(x) for x in adjlist2])-1
            minconfig=adjlist2
        i+=1
    return mincut, minconfig
def secondVertex(numlist,adjlist3):
    if type(numlist)==int:
        print("Error, int passed.")
        print(numlist)
        print(adjlist3)

    vertex=numlist[random.randint(1,len(numlist)-1)]

    for secondIndex in range(len(adjlist3)):
        if vertex in adjlist3[secondIndex][0]:
            return secondIndex
    print("Error, can't find vertex index")

print("--- %s seconds to run---" % (time.time() - start_time))

