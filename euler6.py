# i7-4870HQ 4 cores, 8 threads, 2.5 GHz -> 3.7 GHz
# real	0m0.038s
# user	0m0.025s
# sys	0m0.010s

# In theory, we could divide the two operations into two seperate processes
# However, the performace of this solution is so quick that multiprocessing
# isn't really warranted

def sum_squares(n):
	n_sum = 0
	for i in range(1, n+1):
		n_sum += i ** 2
	return n_sum

def square_sums(n):
	n_sum = 0
	for i in range(1, n+1):
		n_sum += i
	return n_sum ** 2


if __name__ == '__main__':

	print(square_sums(100) - sum_squares(100))