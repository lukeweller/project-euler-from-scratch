# i7-4870HQ 4 cores, 8 threads, 2.5 GHz -> 3.7 GHz
# real	0m0.037s
# user	0m0.025s
# sys	0m0.009s

from math import sqrt

def check_factor(n):
	if 600851475143 % n == 0:
		return True 
	return False

def check_prime(n):
	for i in range(2,int(sqrt(n))):
		if n % i == 0:
			return False
	return True

if __name__ == '__main__':

	largest_factor = 0

	for i in range(3,int(sqrt(600851475143))):
		if check_factor(i):
			if check_prime(int(600851475143/i)):
				print(int(600851475143/i))
				break
			elif check_prime(i) and i > largest_factor:
				largest_factor = i
	
	print(largest_factor)

