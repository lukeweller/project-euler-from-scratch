# i7-4870HQ 4 cores, 8 threads, 2.5 GHz -> 3.7 GHz

from math import sqrt, ceil
from multiprocessing import Pool

def generate_sum(n):
	return [i + n for i in abundant_numbers if i + n < 28123 ]	

def sum_of_proper_divisors(n):

	sum_of_proper_divisors = 1

	for i in range(2, int(ceil(sqrt(n)))):
		if n % i == 0:
			sum_of_proper_divisors += i
			if n / i != i:
				sum_of_proper_divisors += n / i

	return int(sum_of_proper_divisors)

if __name__ == '__main__':

	global abundant_numbers
	abundant_numbers = [i for i in range(1,28123) if i < sum_of_proper_divisors(i)]

	with Pool() as p:
		results = p.map(generate_sum, abundant_numbers)

	results = set([j for i in results for j in i])

	sum_failures = 0

	for i in range(28123):
		if i not in results:
			sum_failures += i
			print(i)

	print(sum_failures)


