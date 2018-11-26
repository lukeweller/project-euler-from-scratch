# i7-4870HQ 4 cores, 8 threads, 2.5 GHz -> 3.7 GHz
# real	0m0.189s
# user	0m0.310s
# sys	0m0.059s

from multiprocessing import Pool

triangle_str= """75
	95 64
	17 47 82
	18 35 87 10
	20 04 82 47 65
	19 01 23 75 03 34
	88 02 77 73 07 63 67
	99 65 04 28 06 16 70 92
	41 41 26 56 83 40 80 70 33
	41 48 72 33 47 32 37 16 94 29
	53 71 44 65 25 43 91 52 97 51 14
	70 11 33 28 77 73 17 78 39 68 17 57
	91 71 52 38 17 14 91 43 58 50 27 29 48
	63 66 04 68 89 53 67 30 73 16 69 87 40 31
	04 62 98 27 23 09 70 98 73 93 38 53 60 04 23""".replace('\t', '').replace('\n', ',').split(',')

triangle_array = []
for line in triangle_str:
	line_arr = line.split(' ')
	triangle_array.append(line_arr)

def find_path_sum(path):

	path_sum = 75
	i = 0
	index = 1

	for bit in path:
		if bit == '1':
			i += 1
		path_sum += int(triangle_array[index][i])
		index += 1

	return path_sum

if __name__ == '__main__':

	n_paths = 2 ** (len(triangle_array) - 1)
	paths = [ str(bin(i))[2:] for i in range(n_paths)]
	
	p = Pool()
	results = p.map(find_path_sum, paths)
	p.close()
	p.join()

	print(max(results))







