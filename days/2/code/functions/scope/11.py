

def fun1(x):
    def fun2(y):
        return x + y
    
    return fun2(1)

print fun1(10)

