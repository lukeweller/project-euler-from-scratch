# i7-4870HQ 4 cores, 8 threads, 2.5 GHz -> 3.7 GHz
# real	0m0.119s
# user	0m0.105s
# sys	0m0.009s

from math import sqrt

def check_triple(x,y):
	if sqrt(x**2 + y**2) % 1 == 0:
		return int(sqrt(x**2 + y**2))
	return False

if __name__ == '__main__':

	break_bool = False

	for a in range(1,400): # 400 found to be fairly good sweet spot in terms of performance; 1000 takes ~ twice as long
		for b in range(1,400):
			c = check_triple(a,b)
			if c != False and a + b + c == 1000:
				print(a*b*c)
				break_bool = True
				break
		if break_bool:
			break