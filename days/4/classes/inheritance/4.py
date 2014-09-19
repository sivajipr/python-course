
class Foo:
    def fun1(self):
        print 'Foo: fun1'

    def fun2(self):
        print 'Foo: fun2'

class Bar(Foo):
    def fun1(self):
        print 'Bar: fun1'

b = Bar()
b.fun1()
b.fun2()
