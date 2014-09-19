
def fun2():
    print 'beginning of fun2 ...'
    try:
        a = 1/0
    except:
        print 'caught ...'

    print 'at the end of fun2 ...'

def fun1():
    fun2()

fun1()

