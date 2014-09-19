import re

s1 = 'this is a nice line'

pat1 = r'n..e'

r = re.search(pat1, s1)

if r:
    print r.group()
