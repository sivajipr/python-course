
def fun2():
    print 'beginning of fun2 ...'
    a = 1/0
    print 'at the end of fun2 ...'

def fun1():
    print 'beginning of fun1 ...'
    try:
        fun2()
    except:
        print 'caught in fun1 ...'

    print 'at the end of fun1 ...'


fun1()

