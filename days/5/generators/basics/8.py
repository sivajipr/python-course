
# return lines having the specified word in them

def grep(lines, word):
    for line in lines:
        if word in line:
            print word


