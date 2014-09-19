import re

s1 = 'this is a nice line!'

pat1 = 'nicely'

# pattern is NOT matched, function returns None
print re.search(pat1, s1)

