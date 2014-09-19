python -m timeit -s 'a={k:k for k in range(100)}' '10 in a'
python -m timeit -s 'a={k:k for k in range(1000)}' '10 in a'
python -m timeit -s 'a={k:k for k in range(10000)}' '10 in a'
python -m timeit -s 'a={k:k for k in range(100000)}' '10 in a'
