import re

s1 = 'This number, 12389 and also this one 7819, one more 765413'

pat1 = r'\d+'

#\d matches single occurrence of a decimal digit (0, 1, ... 9)
r = re.findall(pat1, s1)

print r
