
def small_lines(filename, n):
    for line in open(filename):
        if len(line) < n:
            yield line

def grep(lines, word):
    for line in lines:
        if word in line:
            yield line



result = grep(small_lines('data.txt', 10), 'ok')

for line in result:
    print line
