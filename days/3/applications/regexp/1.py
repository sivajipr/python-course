import re

s1 = 'this is a nice line!'

pat1 = 'nice'

#pattern is matched - returns a "match object"

print re.search(pat1, s1)

