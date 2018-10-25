# i7-4870HQ 4 cores, 8 threads, 2.5 GHz -> 3.7 GHz
# real	0m0.185s
# user	0m0.066s
# sys	0m0.043s

from multiprocessing import Pool

def sum_multiples(n):
	sum_multiples = 0
	for i in range(0,1000,n):
		sum_multiples += i
	return sum_multiples

def remove_duplicates(sum_multiples):
	for i in range(0,1000,3):
		if i % 5 == 0:
			sum_multiples -= i
	return sum_multiples

if __name__ == '__main__':

	p = Pool()
	sum_multiples = sum(p.map(sum_multiples, [3,5]))
	p.close()
	p.join()
	print(remove_duplicates(sum_multiples))
	

