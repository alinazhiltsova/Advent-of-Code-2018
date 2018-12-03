numbers = open('adventday1.txt')
advent = numbers.read().split('\n')
print(sum([int(i) for i in advent]))