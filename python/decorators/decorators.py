import inspect	
def logger(obj):        
	if inspect.isfunction(obj) or inspect.ismethod(obj): 
		def wrapper(*args, **kwargs):
			print 'Entering [---%s---]' % obj.__name__
			obj(*args, **kwargs)
			print 'Leaving [---%s---]\n' % obj.__name__
		wrapper.__name__ = obj.__name__
		return wrapper
	elif inspect.isclass(obj):
		for name, m in inspect.getmembers(obj, inspect.ismethod): 
			setattr(obj, name, logger(m))
		return obj
	return wrapper

@logger
class MyClass():
	def method_without_arg(self):
		print "In method_without_arg" 

	def method_with_arg(self, arg):
		print "In method_with_arg", " with value arg =" , arg

@logger
def func_with_arg(*args, **kwargs):
	print 'In func_with_arg'
	for arg in args:
		print arg
	for kwarg in kwargs:
		print kwarg, '=', kwargs[kwarg]
	
@logger
def func_without_arg():
	print 'In func_without_arg'
	
if __name__=='__main__':	
	my_obj = MyClass()
	my_obj.method_without_arg()
	my_obj.method_with_arg(1)
	func_with_arg(1, 2, 3, 4, 'string_arg', namedarg = 'value')
	func_without_arg()
