# i7-4870HQ 4 cores, 8 threads, 2.5 GHz -> 3.7 GHz
# real	0m0.038s
# user	0m0.026s
# sys	0m0.009s

from math import factorial as fact

def sum_of_digits(n):
	sum_of_digits = 0
	for digit in str(n):
		sum_of_digits += int(digit)
	return sum_of_digits

if __name__ == '__main__':

	print(sum_of_digits(fact(100)))
