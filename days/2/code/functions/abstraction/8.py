


def sigma(term, a, next, b):
    s = 0
    while(a <= b):
        s = s + term(a)
        a = next(a)
    
    return s

print sigma(lambda x:x, 1, lambda x: x+1, 4)

print sigma(lambda x:x*x, 1, lambda x: x+1, 4)

print sigma(lambda x:x*x, 1, lambda x: x+2, 6)

print sigma(lambda x:1.0/(x*(x+2)), 1, lambda x: x+4, 1000)

