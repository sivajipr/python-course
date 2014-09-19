
def sqr(x): return x*x
def cube(x): return x*x*x

def differential(f):
    return lambda x: (f(x + 0.0001) - f(x))/0.0001



g = differential(sqr)

print g(3)

h = differential(cube)

print h(2)


