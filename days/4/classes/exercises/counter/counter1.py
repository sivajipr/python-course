class Counter():
	def __init__(self,n):
		self.n=n
	def increment(self):
		self.n+= 1
	def decrement(self):
		self.n -= 1
	def show(self):
		print self.n

a=Counter(5)
a.show()
a.increment()
a.show()
a.decrement()
a.show()
