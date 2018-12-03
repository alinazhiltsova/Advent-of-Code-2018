numbers = open('adventday1.txt')
advent = numbers.read().split('\n')
print(sum([int(i) for i in advent]))

seen = set()
f = 0
while True:
	for i in advent:
		f+= int(i)
		if f in seen:
			print(f)
			quit()
		seen.add(f)