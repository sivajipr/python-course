

def scale_x(file, n):
    with open(file, 'a+') as f:
        x = int(f.readline())
        t = x / n
        f.write(str(t) + '\n')

try:
    scale_x('data.txt', 0)
except:
    print 'zero division error caught ...'

    
