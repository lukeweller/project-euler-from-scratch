# i7-4870HQ 4 cores, 8 threads, 2.5 GHz -> 3.7 GHz
# real	0m0.745s
# user	0m0.133s
# sys	0m0.030s

import requests

def string_value(s):
	string_sum = 0
	for char in s:
		string_sum += ord(char) - 64
	return string_sum

if __name__ == '__main__':

	response = requests.get('https://projecteuler.net/project/resources/p022_names.txt')
	names_list = response.text.replace('\"', '').split(',')
	names_list.sort()

	score_sum = 0

	for i in range(0, len(names_list)):
		score_sum += string_value(names_list[i]) * (i + 1)

	print(score_sum)

