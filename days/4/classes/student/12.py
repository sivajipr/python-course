
class Student:
    def __init__(self, name, age, rank):
        self.name = name
        self.age = age
        self.rank = rank

    def __str__(self):
        return 'name = %s, age = %d, rank = %d' % (self.name, self.age, self.rank)

    def lower(self, other):
        if self.rank > other.rank:
            return True
        else:
            return False

    
student1 = Student('John', 20, 100)

student2 = Student('Ram', 19, 120)


# check whether student1's rank is lower than student2's rank


s = student1.lower(student2)

print s
