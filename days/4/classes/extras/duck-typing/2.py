
class Duck:
    def quack(self):
        print 'Duck: quack quack'

class LooksLikeADuck:
    def quack(self):
        print 'LooksLikeADuck: quack quack'

    def run(self):
        print 'LooksLikeADuck: run'


def handle_duck(d):
    d.quack()


d = LooksLikeADuck()
handle_duck(d)
