x = 100
class Foo:
    x = 150
    def __init__(self):
        self.x = 10
    def show(self):
        print x

a = Foo()
a.show()

