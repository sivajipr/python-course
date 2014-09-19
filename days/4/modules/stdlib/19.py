from datetime import date

now = date.today()

print now

birthday = date(1975, 5, 21)

age = now - birthday

print 'age = %d days' % age.days


