import math, time
start_time = time.time()
#takes as input newline-separated integers
infile=""
rawdata=open(infile,"r+")
lines=rawdata.read().split('\n')
rawdata.close()

lines.remove('')
lines1=[int(x) for x in lines]

target=range(-10000,10001)
#twoSumHash computes the number of pairs of integers with sum in the target range. 
#bucketsize is chosen based on the input data to make the hash table computation tractable
def twoSumHash(numbers,targ,bucketsize):
    hashtab={x//bucketsize:[] for x in numbers}
    checks={x:0 for x in targ}

    for x in numbers:
        hashtab[x//bucketsize].append(x)
    print("--- %s seconds to load---" % (time.time() - start_time))

    print("beginning seek")
    #need to pick correct keys. this works, i guess
    for key1 in hashtab:
        for key2 in [-key1-2,-key1-1,-key1]:
            for value1 in hashtab[key1]:
                try:
                    for value2 in hashtab[key2]:
                        try:
                           if checks[value1+value2]==0:
                               checks[value1+value2]=1
                        except KeyError:
                            pass
                except KeyError:
                    pass
    return sum(checks.values())


print(twoSumHash(lines1,target,1000000))
print("--- %s seconds to run---" % (time.time() - start_time))
