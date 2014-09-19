
import bisect

a = [10, 25, 27, 28, 28, 31, 33, 41, 50]

print bisect.bisect_left(a, 28)
print bisect.bisect_right(a, 28)

