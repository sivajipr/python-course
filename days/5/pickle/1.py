
import pickle

fruits = {'mango' : 100, 'apple' : 90, 'orange' : 50}

f = open('fruits.p', 'w')

pickle.dump(fruits, f)


