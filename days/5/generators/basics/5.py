
def countdown(n):
    while n > 0:
        yield n
        n -= 1

c = countdown(3)

print c.next()

c.close()

print c.next()
