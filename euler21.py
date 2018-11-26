# i7-4870HQ 4 cores, 8 threads, 2.5 GHz -> 3.7 GHz
# real	0m0.125s
# user	0m0.112s
# sys	0m0.009s

from math import ceil, sqrt

def sum_of_proper_divisors(n):

	sum_of_proper_divisors = 1

	for i in range(2, int(ceil(sqrt(n)))):
		if n % i == 0:
			sum_of_proper_divisors += i
			if n / i != i:
				sum_of_proper_divisors += n / i

	return int(sum_of_proper_divisors)

if __name__ == '__main__':

	amicable_numbers = 0

	for i in range(1, 10000):
		a_pair = sum_of_proper_divisors(i)
		if sum_of_proper_divisors(a_pair) == i and a_pair != i:
			amicable_numbers += i

	print(amicable_numbers)
