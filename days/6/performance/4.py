import timeit


def create2(a, n):
    for i in xrange(n):
        a.insert(0, 0)
    return a

print timeit.timeit("create2([], 10000000)", setup="from __main__ import create2", number=1)

       

