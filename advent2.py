IDs = open('input2.txt')
advent2 = IDs.read().split('\n')

two = 0
three = 0

for string in advent2:
	d = {}
	for letter in string:
		if letter in d:
			d[letter] += 1
		else:
			d[letter] = 1
	for k, v in d.items():
		if v == 2:
			two += 1
			break
	for k, v  in d.items():
		if v == 3:
			three += 1
			break

answer = (two*three)
print(answer)





