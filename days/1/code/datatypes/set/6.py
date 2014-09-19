a = [1,10,1,2,3,2,5,6,3,3,1]

b = {x for x in a if a.count(x) >= 2}

print b
