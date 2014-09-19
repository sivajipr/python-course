
def fun1():
    x = 1
    return lambda y: x + y
    

f = fun1()

x = 10

print f()
