
f = open('data2.txt')

lines = (t.strip() for t in f)

comments = (t for t in lines if t[0] == 'A')

for line in comments:
    print line
