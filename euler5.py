# i7-4870HQ 4 cores, 8 threads, 2.5 GHz -> 3.7 GHz
# real	0m4.359s
# user	0m4.340s
# sys	0m0.013s

# This one definitely has room for improvement
# Need to be able to utilize more than one process

def check_n(n):
	primes_less_than_20 = [19,18,17,16,15,14,13,12,11]
	for prime in primes_less_than_20:
		if n % prime != 0:
			return False
	return True

if __name__ == '__main__':

	n = 0

	while True:
		n += 20
		if check_n(n):
			print(n)
			break



