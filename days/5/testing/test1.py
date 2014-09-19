from nose.tools import *

def fact(n):
    if (n == 0): return 1
    else: return n * fact(n - 1)

def test_fact(): 
    assert_equal(fact(0), 1)
    assert_equal(fact(1), 1)
    assert_equal(fact(2), 2)
    assert_equal(fact(5), 120)


def fun():
    assert False
