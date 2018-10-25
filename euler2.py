# i7-4870HQ 4 cores, 8 threads, 2.5 GHz -> 3.7 GHz
# real	0m0.038s
# user	0m0.025s
# sys	0m0.009s

if __name__ == '__main__':

	curr = [1,2]

	fib_sum = 2

	while curr[1] < 4000000:
		curr_sum = sum(curr)
		curr[0] = curr[1]
		curr[1] = curr_sum
		if curr[1] % 2 == 0 and curr[1] < 4000000:
			fib_sum += curr[1]

	print(fib_sum)