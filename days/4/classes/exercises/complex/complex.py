# A complex number class

class MyComplex:
    pass

c = MyComplex(1, 2) 
d = MyComplex(3, 4)
e = c.add(d)
print c.re, c.im # prints 4, 6

print c # prints (4 + 6j) # implement the __str__ method

e = c + d # implement the __add__ method

print e 

