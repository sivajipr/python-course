
class Student:
    def __init__(self, name, score):
        self.name = name
        self.score = score


s = Student('ravi', 100)

print s.__dict__

