class Rectangle:
	def __init__(self,c,d):
		self.c = c
		self.d = d
	def __str__(self):
		return 	'~~You are doing class Rectangle~~'
	def smaller(self,name):
		if (self.c * self.d) < (name.c * name.d):
			return True
		else:
			return False


a = Rectangle(3, 4)

b = Rectangle(4, 5)
print b
print a<b
print a>b
