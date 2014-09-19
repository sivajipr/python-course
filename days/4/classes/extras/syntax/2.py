class Foo:
    pass


def fun(f):
    f.x = 1

fun(Foo)

print Foo.x
