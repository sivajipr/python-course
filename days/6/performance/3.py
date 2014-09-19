import timeit


def create(a, n):
    for i in xrange(n):
        a.append(0)
    return a

print timeit.timeit("create([], 10000000)", setup="from __main__ import create", number=1)

       

