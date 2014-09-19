
try:
    a = 1/0
except NameError:
    print 'symbol does not exist'
except ZeroDivisionError:
    print 'divide by zero error'

