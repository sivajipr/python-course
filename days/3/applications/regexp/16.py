import re

s1 = 'My number: 98913487. Please do not call'

pat1 = r'\d+'

#\d matches single occurrence of a decimal digit (0, 1, ... 9)
r = re.search(pat1, s1)

if r:
    print r.group()
