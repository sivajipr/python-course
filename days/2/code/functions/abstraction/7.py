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

def sum_odd_cubes(a, b):
    s = 0
    while (a <= b):
        s = s + a*a*a
        a = a + 2
    
    return s


def sum_pi_series(a, b):
    s = 0
    while(a <= b):
        s = s + 1.0/(a * (a+2))
        a = a + 4

    return s

print sum_pi_series(1, 1000)

