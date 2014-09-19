fields = (line.split() for line in open('student.txt'))

db = ({'name' : f[0],
       'age'  : int(f[1]),
       'rank' : int(f[2])} for f in fields)


top10 = ((s['name'], s['rank']) for s in db if s['rank'] < 10)

for name in top10:
    print name

