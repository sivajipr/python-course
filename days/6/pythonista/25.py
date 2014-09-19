
all_students = ['john', 'ravi', 'hari', 'rahul', 'joseph']

d = {'john':100, 'hari':20, 'rahul':99}

for name in all_students:
    if name not in d:
        d[name] = 0
    d[name] += 1

print d


    


