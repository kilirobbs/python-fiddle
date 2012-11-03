from multiprocessing import Pool
import multiprocessing

def f(x):
	print multiprocessing.current_process()
	return x*x

if __name__ == '__main__':
	print "1"
	pool = Pool(processes=1)
	result = pool.apply_async(f, [10], None)

p = multiprocessing.Pool()
print p.map(f, range(6))