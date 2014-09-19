
f_saved = None

def fun():
    global f_saved
    with open('data.txt') as f:
        print f.readline()
        f_saved = f
        x = 1/0
try:
    fun()
except ZeroDivisionError:
    print f_saved.readline()

