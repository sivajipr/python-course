import test2
total_functions=0
passed_functions=0
symbols = dir(test2)
for symbol in symbols:
	f=getattr(test2,symbol)
	if callable(f) and symbol.startswith('test'):
		total_functions=total_functions + 1
		if f():
			passed_functions=passed_functions + 1

print 'total_functions =%d, passed_functions =%d' %(total_functions,passed_functions)
