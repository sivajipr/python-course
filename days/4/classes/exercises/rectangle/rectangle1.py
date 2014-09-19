class Rectangle:
	def __init__(self,l,b):
		self.l=l
		self.b=b
	def __str__(self,other):
		return(self.l*self.b)<(other.l*other.b)



a=Rectangle(4,5)
b=Rectangle(2,3)
t=a<b
print t
