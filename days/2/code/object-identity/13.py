import copy

a = [1,2,[3,4]]
b = copy.deepcopy(a)

print a is b

b[0] = 10
print a

b[2][0] = 10
print a
