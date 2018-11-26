# i7-4870HQ 4 cores, 8 threads, 2.5 GHz -> 3.7 GHz
# real	0m0.039s
# user	0m0.026s
# sys	0m0.009s

dict_0 = {0: '', 1: 'one', 2: 'two', 3: 'three', 4: 'four', 5: 'five', 6: 'six', 7: 'seven', 8: 'eight', 9: 'nine'}
dict_teens = {10: 'ten', 11: 'eleven', 12: 'twelve', 13: 'thirteen', 14: 'fourteen', 15: 'fifteen', 16: 'sixteen', 17: 'seventeen', 18: 'eighteen', 19: 'nineteen' }
dict_10 = {0: '', 2: 'twenty', 3: 'thirty', 4: 'forty', 5: 'fifty', 6: 'sixty', 7: 'seventy', 8: 'eighty', 9: 'ninety'}

def compile_str(n):

	str_n = str(n)
	while len(str_n) < 3: 
			str_n = '0' + str_n

	p100 = str_n[0]
	p10 = str_n[1]
	p1 = str_n[2]

	word_str = ''

	if n > 99:
		word_str += dict_0[int(p100)] + 'hundred'
		if p10 != '0' or p1 != '0':
			word_str += 'and'

	if p10 == '1':
		word_str += dict_teens[int(p10+p1)]
	else:
		word_str += dict_10[int(p10)]
		word_str += dict_0[int(p1)]

	return word_str


if __name__ == '__main__':

	letter_count = len('onethousand')

	for i in range(1, 1000):

		letter_count += len(compile_str(i))

	print(letter_count)




