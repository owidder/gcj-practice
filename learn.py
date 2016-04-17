def f(a, b):
    def g(c):
        print(a*b + c)

    return g


f(3,4)(10)
f(3,4)(20)