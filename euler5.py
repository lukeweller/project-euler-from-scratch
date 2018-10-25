# i7-4870HQ 4 cores, 8 threads, 2.5 GHz -> 3.7 GHz
# real	0m0.261s
# user	0m0.248s
# sys	0m0.009s

def check_n(n):
	primes_less_than_20 = [18,17,16,15,14,13,12,11]
	for prime in primes_less_than_20:
		if n % prime != 0:
			return False
	return True

if __name__ == '__main__':

	n = 0

	while True:
		n += (20*19)
		# The above line **vastly** increases the performace of the solution
		# However, it should be noted that it makes the solution no longer "perfect",
		# as it is possbile for a solution to not be factorable by (20 * 19)
		# If we instead used 'n += 20', it would be a perfect solution, but perforamce
		# takes a huge hit; the solution takes x10 longer.
		if check_n(n):
			print(n)
			break
