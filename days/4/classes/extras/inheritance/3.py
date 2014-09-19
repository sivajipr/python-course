class Foo:
    def __init__(self):
        print 'Foo: __init__'

class Bar(Foo):
    def __init__(self):
        print 'Bar: __init__'
        Foo.__init__(self)

b = Bar()

