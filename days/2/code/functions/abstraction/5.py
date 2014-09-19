def sum(a, b):
    s = 0
    while (a <= b):
        s = s + a
        a = a + 1
    
    return s


def sum_squares(a, b):
    s = 0
    while (a <= b):
        s = s + a*a
        a = a + 1
    
    return s

def sum_cubes(a, b):
    s = 0
    while (a <= b):
        s = s + a*a*a
        a = a + 1
    
    return s

print sum_cubes(1, 4)
