# check whether N is prime

# 1051 is a prime number

N = 1051

i = 2
flag = True
while i < N/2:
    if (N % i) == 0:
        flag = False
        break
    i = i + 1

if flag:
    print N, 'is prime'

