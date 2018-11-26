# i7-4870HQ 4 cores, 8 threads, 2.5 GHz -> 3.7 GHz
# real	0m0.036s
# user	0m0.025s
# sys	0m0.009s

if __name__ == '__main__':

	sum_digits = 0
	n_str = str(2**1000)
	for digit in n_str:
		sum_digits += int(digit)
	print(sum_digits)