
# We start from the result that for small values
# of `x', e**x = 1 + x.
# Assume that e**(i*x) = 1 + (i*x), where `i' represents
# imaginary part of a complex number.

#Now, what is e**(2*i*x)? It is (1 + (i*x)) * (1 + (i*x))
#or, (1 + (i*x)) ** 2
#What is e**(3*i*x)? It is (1 + (i*x))**3 and so on ...

#We are going to set x = (2*pi/1000) and generate the following
#values: (1 + 0.00628*i), (1 + 0.00628*i)**2, (1 + 0.00628*i)**3
#and so on till (1 + 0.00628*i)**1000.
#This corresponds to values from e**[i*((2*pi)/1000)] to e**(i*2*pi)
 
from pylab import *


#Write a comprehension which will produce the following list:
#[(1+0.00628*i)**1, (1+0.00628*i)**2, (1+0.00628*i)**3, ... (1+0.00628*i)**1000]

a = 

#Now, extract the real parts of each element of `a' into another 
#list `b'

b = 

#Extract the imaginary parts of each element of `a' into another
#list `c':

c = 

plot(b)
show()

plot(c)
show()


