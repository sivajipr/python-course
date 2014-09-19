
all_students = ['john', 'ravi', 'hari', 'rahul', 'joseph']

d = {'john':100, 'hari':20, 'rahul':99}

for name in all_students:
    d[name] = d.get(name, 0) + 1

print d


    


