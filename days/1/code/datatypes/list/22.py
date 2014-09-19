a = [1,2,3,4]

t = [(u, v) for u in a for v in a if (u - v) == 1]

print t
