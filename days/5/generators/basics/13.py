
f = open('data2.txt')

lines = (t.strip() for t in f)

for line in lines:
    print line
