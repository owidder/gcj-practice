import sys

infile = open(sys.argv[1] + ".in", "r")
outfile = open(sys.argv[1] + ".out", "w")

def findItems(C, items):
    for i1 in range(0, len(items)-1):
        for i2 in range(i1+1, len(items)):
            if(items[i1] + items[i2] == C):
                return (i1, i2)


def nextTestCase(i):
    C = int(next(infile))
    I = int(next(infile))
    items = [int(x) for x in next(infile).rstrip().split(" ")]
    (i1, i2) = findItems(C, items)
    outfile.write("Case #%s: %s %s\n" % (i+1, i1+1, i2+1))


N = int(next(infile))
for i in range(0, N):
    nextTestCase(i)