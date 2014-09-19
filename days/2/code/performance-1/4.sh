python -m timeit -s 'a=tuple(range(100))' '(-10) in a'
python -m timeit -s 'a=tuple(range(1000))' '(-10) in a'
python -m timeit -s 'a=tuple(range(10000))' '(-10) in a'
python -m timeit -s 'a=tuple(range(100000))' '(-10) in a'
