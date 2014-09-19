
def fun():
    print 'before ...'
    try:
        a = 1/0
    except:
        print 'caught ...'


fun()

