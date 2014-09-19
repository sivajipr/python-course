import test1


for symbol in dir(test1):
    attr = getattr(test1, symbol)
    if (callable(attr) and attr.__name__.startswith('test')):
        attr()


