
class Student:
    def __init__(self, name, score):
        self.name = name
        self.score = score


s = Student('ravi', 100)

print 'hello %(name)s, your score is %(score)d' % s.__dict__


