import sys

a = []
print sys.getrefcount(a)

b = a
print sys.getrefcount(a)

c = b
print sys.getrefcount(a)

del b
print sys.getrefcount(a)

del c
print sys.getrefcount(a)
