class Rectangle:
	def __init__(self, l,b):
		self.le=l
		self.br=b
	def __lt__(self,other):
		return (self.le*self.br)<(other.le*other.br)









a=Rectangle(3,4)
b=Rectangle(4,5)
t=a<b
print t
