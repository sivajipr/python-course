class Counter:
	def __init__(self,count):
		self.i=0
		self.count=count
	def __str__(self):
		return "counter:%d" %(self.i)
	def show(self):
		print self.count
	def increment(self):
		self.i += 1
	def decrement(self):
		self.i -= 1
		
		

#c = Counter()
#c.show() # prints 0.
#c.increment()
#c.show() # prints 1
#c.decrement() 
#c.show() # prints 0
#print c # prints 'Counter: 0' (implement the __str__ method)
c = Counter(10) # __init__ should accept an argument
c.show() # prints 10
