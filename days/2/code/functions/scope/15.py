
x = 1

def fun1():
    x = 10
    def fun2():
        x = 20
        def fun3():
            print x
        fun3()
    fun2()

fun1()


