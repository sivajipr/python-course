
class Duck:
    def quack(self):
        print 'Duck: quack quack'


def handle_duck(d):
    d.quack()


d = Duck()
handle_duck(d)
