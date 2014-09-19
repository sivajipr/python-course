
def fun1():
    print 'fun1 ...'

def fun2():
    print 'fun2 ...'


def fun3():
    print 'fun3 ...'

def fun4():
    print 'fun4 ...'



def print_msg(f):
    def new_f():
        print 'Beginning of function ...'
        f()
    return new_f

fun2 = print_msg(fun2)
fun4 = print_msg(fun4)

fun2()

