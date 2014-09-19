python -m timeit -s 'a=set(range(100))' '(-10) in a'
python -m timeit -s 'a=set(range(1000))' '(-10) in a'
python -m timeit -s 'a=set(range(10000))' '(-10) in a'
python -m timeit -s 'a=set(range(100000))' '(-10) in a'
