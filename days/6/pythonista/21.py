# Can't avoid use of "in" here


d = {'john':100, 'hari':20, 'rahul':99}

for name in d:
    d[name + '_new'] = 0

print d
    
