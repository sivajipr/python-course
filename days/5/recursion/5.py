
def null(xs):
    return len(xs) == 0

def head(xs):
    return xs[0]

def tail(xs):
    return xs[1:]


def cons(x, xs):
    return [x] + xs

def is_even(x):
    return x%2 == 0

def filter_even(xs):
    # return new list composed of only even numbers from xs


print filter_even([1,2,3,4])


