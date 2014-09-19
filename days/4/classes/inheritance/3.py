
class Foo:
  def fun1(self):
    print 'Foo: fun1'

class Bar(Foo):
  def fun2(self):
    print 'Bar: fun2'

b = Bar()
b.fun1()
