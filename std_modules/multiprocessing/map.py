import multiprocessing

def f(x):
	print multiprocessing.current_process()
	return x*x

p = multiprocessing.Pool()
print p.map(f, range(6))