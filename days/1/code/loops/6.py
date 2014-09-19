# check whether N is prime

# 1051 is a prime number

N = 1051

i = 2
while i < N/2:
    if (N % i) == 0:
        break
    i = i + 1

else:
    print N, 'is  prime'

