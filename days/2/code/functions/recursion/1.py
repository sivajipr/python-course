
def count(n):
    if (n == 0):
        return
    else:
        print n
        count(n - 1)

count(10000)
