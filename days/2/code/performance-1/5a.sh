python -m timeit -s 'a=set(range(100))' '(99) in a'
python -m timeit -s 'a=set(range(1000))' '(999) in a'
python -m timeit -s 'a=set(range(10000))' '(9999) in a'
python -m timeit -s 'a=set(range(100000))' '(99999) in a'
