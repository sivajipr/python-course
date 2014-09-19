
try:
    a = b
except NameError:
    print 'symbol does not exist'
except ZeroDivisionError:
    print 'divide by zero error'

