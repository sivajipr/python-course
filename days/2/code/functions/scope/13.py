
x = 1

def fun1():
    x = 10
    def fun2():
        global x
        print x
    fun2()

fun1()


