# i7-4870HQ 4 cores, 8 threads, 2.5 GHz -> 3.7 GHz
# real	0m1.680s
# user	0m1.617s
# sys	0m0.053s

# Performance here is definitely not optimal, but I can't think
# of a way to implement a sieve with multiprocessing

from math import sqrt

def generate_sieve(n):
	sieve = [ i for i in range(n)]

	remove_int = 2
	i = 2

	while remove_int < sqrt(len(sieve)):
		while (remove_int * i) < len(sieve):
			sieve[remove_int*i] = 0
			i += 1
		i = 2
		remove_int += 1
		while(sieve[remove_int] == 0):
			remove_int += 1
			if remove_int >= len(sieve):
				break

	return sieve[2:]

if __name__ == '__main__':

	print(sum(generate_sieve(2000000)))