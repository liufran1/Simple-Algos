import itertools
from fractions import Fraction

vectors = ['1111000000','0100100101','0000011110','0111111111','1011111111']

def jaccardDistance(vector1,vector2):    
    #convert to binary
    bin1 = int(vector1, base = 2)
    bin2 = int(vector2, base = 2)
    
    #print("Vector1: %d" %bin1)
    #print("Vector2: %d" %bin2)
    #intersection
    intersection = bin(bin1 & bin2)
    #print("Intersection: %s" %intersection)
    #union    
    union = bin(bin1 | bin2)
    #print("Union: %s" %union)    
    return 1 - Fraction(intersection.count('1'),union.count('1'))

print("Jaccard Distances: ")
for pair in itertools.product(vectors, repeat=2):
    print(jaccardDistance( *pair))

def manhattanDistance(vector1,vector2):
    #take abs of diff of each entry
    bin1 = int(vector1, base = 2)
    bin2 = int(vector2, base = 2)
    
    distance = bin(bin1 ^ bin2)
    #return sum
    return distance.count('1')

manhattanVect = {n:0 for n in range(11)}    
print("Manhattan Distances: ")
for pair in itertools.product(vectors, repeat=2):
    print("Input: ")
    print(pair)
    print("Distance: ")
    print(manhattanDistance(*pair))
    manhattanVect[manhattanDistance(*pair)]+=1

print(manhattanVect)

def levenshteinDistance(s1, s2):
    if len(s1) > len(s2):
        s1, s2 = s2, s1

    distances = range(len(s1) + 1)
    for i2, c2 in enumerate(s2):
        distances_ = [i2+1]
        for i1, c1 in enumerate(s1):
            if c1 == c2:
                distances_.append(distances[i1])
            else:
                distances_.append(1 + min((distances[i1], distances[i1 + 1], distances_[-1])))
        distances = distances_
    return distances[-1]
    
editVect = []
editDist = {n:0 for n in range(6)}    

for pair in itertools.product(editVect, repeat=2):
    print("Input: ")
    print(pair)
    print("Distance: ")
    print(levenshteinDistance(*pair))
    editDist[levenshteinDistance(*pair)]+=1

print(editDist)