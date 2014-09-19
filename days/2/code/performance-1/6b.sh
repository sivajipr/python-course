python -m timeit -s 'a={k:k for k in range(100)}' '11 in a'
python -m timeit -s 'a={k:k for k in range(1000)}' '123 in a'
python -m timeit -s 'a={k:k for k in range(10000)}' '1783 in a'
python -m timeit -s 'a={k:k for k in range(100000)}' '56192 in a'
