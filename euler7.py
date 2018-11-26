# i7-4870HQ 4 cores, 8 threads, 2.5 GHz -> 3.7 GHz
# real	0m0.185s
# user	0m0.167s
# sys	0m0.014s

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

def find_n_prime(sieve, n):
	counter = 0
	for i in sieve:
		if i != 0:
			counter += 1
		if counter == n:
			return i
	return False

if __name__ == '__main__':

	sieve_size = 200000 # Guess and check used to estimate optimal sieve size for perfomance; any larger number would also work, but at the cost of performance
	n = 10001
	print(find_n_prime(generate_sieve(sieve_size), n))

	


