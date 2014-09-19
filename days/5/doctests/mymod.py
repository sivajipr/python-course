
def my_max(a, b):
    """Compute maximum of two numbers, a and b.
    >>> my_max(1, 2)
    2
    >>> my_max(1, 1)
    1
    >>> my_max(20, 10)
    20
    >>>
    """

    return b if (a > b) else a


if __name__ == '__main__':
    import doctest
    doctest.testmod()
