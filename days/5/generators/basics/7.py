
#return list of lines less than length "n"

def small_lines(filename, n):
    result = []
    for line in open(filename):
        if len(line) < n:
            result.append(line)
    return result

r = small_lines('data.txt', 10)

for line in r:
    print line



