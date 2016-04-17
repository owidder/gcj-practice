import sys

infile = open(sys.argv[1] + ".in", "r")
outfile = open(sys.argv[1] + ".out", "w")

def nextTestCase(i):
    words = next(infile).rstrip().split(" ")
    words.reverse()
    outfile.write("Case #%s: %s\n" % (i+1, " ".join(words)))


N = int(next(infile))
for i in range(0, N):
    nextTestCase(i)
