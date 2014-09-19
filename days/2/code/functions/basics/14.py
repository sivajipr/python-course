
def fact(n):
    f = 1
    while n > 0:
        f = f * n
        n = n - 1
    return f

print fact(0)
print fact(1)
print fact(5)
