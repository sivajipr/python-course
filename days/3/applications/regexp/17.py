import re

s1 = '1296:2356'

pat1 = r'\d+:\d+'

#\d matches single occurrence of a decimal digit (0, 1, ... 9)
r = re.search(pat1, s1)

if r:
    print r.group()
