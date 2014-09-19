
class Student:
    def __init__(self, name, age, rank):
        self.name = name
        self.age = age
        self.rank = rank

    def __str__(self):
        return 'name = %s, age = %d, rank = %d' % (self.name, self.age, self.rank)

student1 = Student('John', 20, 100)

print student1
