# i7-4870HQ 4 cores, 8 threads, 2.5 GHz -> 3.7 GHz
# real	0m12.117s
# user	1m31.932s
# sys	0m0.253s

from multiprocessing import Pool

def collatz(n):
	if n % 2 == 0:
		return n / 2
	return 3 * n + 1

def len_collatz_str(n):
	seq_len = 1
	while n != 1:
		n = collatz(n)
		seq_len += 1
	return seq_len

def search_for_max_chain(results):
	max_len = 0
	max_len_register = 0

	for i in range(len(results)):
		if  results[i] > max_len:
			max_len = results[i]
			max_len_register = i

	return max_len_register

if __name__ == '__main__':

	upper_limit = 1000000
	max_len = 0
	max_len_register = 0

	with Pool() as p:
		results = p.map(len_collatz_str, [ i for i in range(1,upper_limit)])

	print(search_for_max_chain(results))
