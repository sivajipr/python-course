import re

s1 = 'is this a nice line?'

pat1 = r'^is'

r=re.search(pat1, s1)
if r:
	print r.group()
