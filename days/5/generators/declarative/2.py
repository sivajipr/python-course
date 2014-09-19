fields = (line.split() for line in open('student.txt'))

db = ({'name' : f[0],
       'age'  : f[1],
       'rank' : f[2]} for f in fields)

for item in db:
    print item

