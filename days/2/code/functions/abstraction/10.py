
def add_n(n):
    return lambda x: x + n

add_two = add_n(2)

print add_two(10)
