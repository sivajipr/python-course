class Complex:
	def __init__(self,r,i):
		self.r=r
		self.i=i
	def add(self,other):
		k=self.r+other.r
		l=self.i+other.i
	def __str__(self):
		return '(%d + %dj)' %(k,l)

a=(5,6)
b=(2,3)
c=a.add(b)
print c
