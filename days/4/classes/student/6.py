
class Student:
    pass

def new_student(name, age, rank):
    s = Student()
    s.name = name
    s.age = age
    s.rank = rank
    return s

student1 = new_student('John', 20, 100)

student2 = new_student('Ram', 19, 120)


# return student whose rank is better

def higher_rank(a, b):
    if a.rank < b.rank:
        return a
    else:
        return b


s = higher_rank(student1, student2)
print s.name, s.age, s.rank

