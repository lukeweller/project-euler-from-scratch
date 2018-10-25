# i7-4870HQ 4 cores, 8 threads, 2.5 GHz -> 3.7 GHz
# real	0m0.389s
# user	0m2.159s
# sys	0m0.047s

from multiprocessing import Pool

def check_palindrome(n):
	n = str(n)
	for i in range(int(len(n)/2)):
		if n[i] != n[len(n)-i-1]:
			return False
	return True

def handle_chunk(range_pairing):
	largest_palidrome = 0
	for a in range(range_pairing[0][0], range_pairing[0][1]):
		for b in range(range_pairing[1][0], range_pairing[1][1]):
			if check_palindrome(a*b) and a*b > largest_palidrome:
				largest_palidrome = a*b
	return largest_palidrome

if __name__ == '__main__':
	
	n_chunks = 4

	# Note 1:
	# Dividing the range into 4 chunks should end up 
	# creating 24 processes (4!) for the muliprocessing
	# pool, giving each logical core an even number of 
	# processes to work through (3).  However, because the processes
	# will end up running at different speeds, the number of
	# chunks is *somewhat* arbitrary.

	# Note 2:
	# Based on manual testing with the linux time command,
	# dividing the range into four chunks is the sweet spot
	# in terms of performance.  Curiously, the pool only 
	# seems to generate around ~17 processes, so my original
	# guess seems to have been simply lucky

	range_size = (999-100)/n_chunks
	ranges = []

	i = 100
	for cores in range(n_chunks):
		ranges.append([int(i),int(i+range_size)])
		i += range_size

	range_pairings = []
	for r0 in ranges:
		for r1 in ranges:
			range_pairings.append([r0,r1])

	p = Pool()
	chunk_largest_palidrome_list = p.map(handle_chunk,range_pairings)
	p.close()
	p.join()

	print(max(chunk_largest_palidrome_list))


	




	# for a in range(1000):
	# 	for b in range(1000):
	# 		if check_palindrome(a*b) and a*b > largest_palidrome:
	# 			largest_palidrome = a*b

	# print(largest_palidrome)

		


