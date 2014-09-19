
try:
    a = 1/0
except ZeroDivisionError:
    print 'caught division by zero error'
else:
    print 'else ...'

