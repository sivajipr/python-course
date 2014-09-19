

def scale_x(file, n):
    f = open(file, 'a+')
    x = int(f.readline())
    t = x / n
    f.write(str(t) + '\n')
    f.close()

try:
    scale_x('data.txt', 0)
except:
    print 'zero division error caught ...'

    
