import sys

infile = open(sys.argv[1], "r")

def findItems(C, items):
    for i1 in range(0, len(items)-1):
        for i2 in range(i1+1, len(items)):
            currentSum = items[i1] + items[i2]
            if(currentSum == C):
                return (i1, i2)
            elif(currentSum > C):
                break



def nextTestCase(i):
    C = int(next(infile))
    I = int(next(infile))
    items = [int(x) for x in next(infile).rstrip().split(" ")]
    items.sort()
    (i1,i2) = findItems(C, items)
    print("Case: #%s: %s %s" % (i, i1+1, i2+1))


N = int(next(infile))
for i in range(0,N):
    nextTestCase(i)