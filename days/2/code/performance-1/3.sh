python -m timeit -s 'a=range(100)' '(-10) in a'
python -m timeit -s 'a=range(1000)' '(-10) in a'
python -m timeit -s 'a=range(10000)' '(-10) in a'
python -m timeit -s 'a=range(100000)' '(-10) in a'
