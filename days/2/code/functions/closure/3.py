
def fun1():
    x = 1
    
    def fun2():
        y = 2
        return x + y
    
    return fun2
    

f2 = fun1()

x = 10

print f2()
