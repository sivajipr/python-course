
def all_integers():
    n = 0
    while True:
        yield n
        n += 1

a = all_integers()

for i in a:
    print i

