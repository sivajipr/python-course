
class Student:
    pass


student1 = Student()
student1.name = 'John'
student1.age = 20
student1.rank = 100

student2 = Student()
student2.name = 'Ram'
student2.age = 19
student2.rank = 120


# return student whose rank is better

def higher_rank(a, b):
    if a.rank < b.rank:
        return a
    else:
        return b


s = higher_rank(student1, student2)
print s.name, s.age, s.rank

