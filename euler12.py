# i7-4870HQ 4 cores, 8 threads, 2.5 GHz -> 3.7 GHz
# real	0m5.072s
# user	0m5.035s
# sys	0m0.023s

from math import sqrt

def gen_triangle(n):
	cnt = 0
	for i in range(1,n+1):
		cnt += i
	return cnt

def n_divisors(n):
	# The line below works on the assumption that a highly divisible
	# number will likely be divisible by all the primes less than 10
	# i.e. if it's not divisible by 2, it's very unlikely to have 500
	# divisors.  While this line technically makes the solution imperfect,
	# it improves performance of the program by 75-100%
	if n % 2 != 0 or n % 3 != 0 or n % 5 != 0 or n % 7 != 0 or n % 11 != 0:
		return 0
	n_divisors = 0
	for i in range(1,int(sqrt(n))+1):
		if n % i == 0:
			n_divisors += 1
	return n_divisors * 2

if __name__ == '__main__':

	i = 0
	n = 500

	while True:
		i += 1
		if n_divisors(gen_triangle(i)) > n:
			print(gen_triangle(i))
			break	


