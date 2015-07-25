import os.path

if os.path.isfile('input.txt'): 
	f = open('input.txt', 'r')
	sq = f.read()
	f.close()
	max_len = 0
	curr_len = 1
	for i in range(0, len(sq)-1):
		this = sq[i]
		if (this == '0'):
			next = sq[i+1]
			if (this == next):
				curr_len += 1
			else:
				curr_len = 1
			if max_len < curr_len:
				max_len = curr_len
	f = open('output.txt', 'w+')
	f.write(str(max_len))
	f.close()