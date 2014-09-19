
def fun1():
    x = 1
    
    def fun2():
        y = 2
        print x
    
    return fun2
    

f2 = fun1()

x = 10

f2()
