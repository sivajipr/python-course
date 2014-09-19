
def sqr(x):
    return x*x

def cube(x):
    return x*x*x

def compose(f, g, x):
    return f(g(x))

print compose(sqr, cube, 2)

