
def is_even(n):
    return (n % 2) == 0

t = filter(is_even, [1, 2, 3, 4, 5, 6])

print t
