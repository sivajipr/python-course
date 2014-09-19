
import doctest

def average(x, y):
    """ Find average of two numbers.

    >>> print average(2, 4)
    3
    >>>
    """
    return (x + y) / 2


doctest.testmod()

