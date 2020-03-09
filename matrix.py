import random as r
import time

symbols = ["0", "", "", ' ']
line = []
counter = 0

for i in range(118):
	x = r.randint(0,3)
	line.append(symbols[x])

	counter += 1

for i in range(10000):
	if counter % 5== 0:
		x_symbols = [r.randint(0,117)for x in range(10)]

		for i in x_symbols:
			line[i] = symbols[r.randint(0,3)]
	print(*line)
	counter += 1
	time.sleep(0.1)
