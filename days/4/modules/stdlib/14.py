import re

a = re.search('ra+b', 'qqraaabmmraaaaaaaaab')
if a:
    print a.group()






