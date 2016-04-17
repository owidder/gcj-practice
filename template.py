import sys

infile = open(sys.argv[1] + ".in", "r")
outfile = open(sys.argv[1] + ".out", "w")

def solve():
    pass


def nextTestCase(i):
    X = solve()
    outfile.write("Case #%s: \n" % (i+1))


N = int(next(infile))
for i in range(0, N):
    nextTestCase(i)