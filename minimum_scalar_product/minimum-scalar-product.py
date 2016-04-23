import sys
import itertools

infile = open(sys.argv[1] + ".in", "r")
outfile = open(sys.argv[1] + ".out", "w")

def dot(X, Y):
    dotProduct = 0
    for i in range(0, len(X)):
        dotProduct += (X[i] * Y[i])
    return dotProduct

def getIntsFromLine(line):
    return [int(x) for x in line.rstrip().split(" ")]

def computeSmallest(X, Y):
    X.sort()
    Y.sort()
    Y.reverse()
    return dot(X, Y)

def nextTestCase(i):
    n = int(next(infile))
    X = getIntsFromLine(next(infile))
    Y = getIntsFromLine(next(infile))
    smallest = computeSmallest(X, Y)
    print("case #%s: %s" % (i+1, smallest))
    outfile.write("Case #%s: %s\n" % (i+1, smallest))


N = int(next(infile))
for i in range(0, N):
    nextTestCase(i)
