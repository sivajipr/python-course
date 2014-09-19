
student1 = ('John', 20, 100)
student2 = ('Ram', 19, 120)
student3 = ('Joseph', 21, 340)

# return student whose rank is better
def higher_rank(a, b):
    if a[2] < b[2]:
        return a
    else:
        return b


print higher_rank(student1, student2)
