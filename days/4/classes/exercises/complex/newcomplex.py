class Complex:
	def __init__(self,r,i):
		self.re=r
		self.im=i
	def __add__(self,other):
		return Complex(self.re+other.re,self.im+other.im)
	def __str__(self):
		return '(%d + %dj)' %(self.re,self.im)

		
		
a = Complex(1,2)
b = Complex(3,4)
c = a+b
print c

