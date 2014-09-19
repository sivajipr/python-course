x = 100
class Foo:
    x = 150
    
    def __init__(self):
        self.x = 10

    def show(self):
        print Foo.x

    def inc(self):
        Foo.x += 1

a = Foo()
a.show()
a.inc()

b = Foo()
b.show()

