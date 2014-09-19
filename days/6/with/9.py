
f_saved = None

def fun():
    global f_saved
    f = open('data.txt')
    print f.readline()
    f_saved = f
    x = 1/0
    f.close()

try:
    fun()
except ZeroDivisionError:
    print f_saved.readline()

