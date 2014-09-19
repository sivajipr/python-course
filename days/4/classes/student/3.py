
student1 = {'name':'John', 'age':20, 'rank':100}
student2 = {'name':'Ram', 'age':19, 'rank':120}
student3 = {'name':'Joseph', 'age':21, 'rank':340}

# return student whose rank is better

def higher_rank(a, b):
    if a['rank'] < b['rank']:
        return a
    else:
        return b


print higher_rank(student1, student2)
