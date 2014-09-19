   
#each line of d.txt is a single word

f = open('d.txt')

w = {}

for word in f:
        r = word.strip()
        if r in w:
           w[r] += 1
        else:
           w[r]=1
print w

# print the key, value pairs in w using a for loop
