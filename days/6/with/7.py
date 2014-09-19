
f_saved = None

def fun():
    global f_saved
    with open('data.txt') as f:
        print f.readline()
        f_saved = f

fun()
print f_saved.readline()

