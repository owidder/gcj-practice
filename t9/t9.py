import sys

infile = open(sys.argv[1] + ".in", "r")
outfile = open(sys.argv[1] + ".out", "w")

def codeForLetter(letter, lastKey):
    code = ""
    keys = [" ", "", "abc", "def", "ghi", "jkl", "mno", "pqrs", "tuv", "wxyz"]
    for key in range(0, len(keys)):
        if(letter in keys[key]):
            if(lastKey != "0" and lastKey == key):
                code += " "
            code += str(key) * (keys[key].find(letter)+1)
            return (code, key)

def codeForText(text):
    key = ""
    textAsCode = ""
    for i in range(0, len(text)):
        (code, key) = codeForLetter(text[i], key)
        textAsCode += code

    return textAsCode


def nextTestCase(i):
    text = next(infile).rstrip("\n")
    code = codeForText(text)
    outfile.write("Case #%s: %s\n" % (i+1, code))


N = int(next(infile))
for i in range(0, N):
    nextTestCase(i)