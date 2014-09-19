
def new_student(name, age, rank):
    return {'name' : name, 'age' : age, 'rank' : rank}

student1 = new_student('John', 20, 100)
student2 = new_student('Ram', 19, 120)
student3 = new_student('Joseph', 21, 340)

# return student whose rank is better

def higher_rank(a, b):
    if a['rank'] < b['rank']:
        return a
    else:
        return b


print higher_rank(student1, student2)
