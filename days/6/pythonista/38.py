# sorting with key

a = ['abc', 'abcdef', 'm']

a.sort(key = len)

print a

b = ['Apple', 'ant']

print sorted(b)

print sorted(b, key = lambda x: x.lower())

c = ["12", "3"]

print sorted(c)

print sorted(c, key=int)

