str = input('Enter your word: ')
new = ''

count = 0
firstVow = 0
num = 0

while count < len(str):
	if str[count] in 'aeiouy':	
		firstVow = count
		while firstVow < len(str):
			new += str[firstVow]
			firstVow += 1
		while num < count:
			new += str[num]
			num += 1
		if str[0] in 'aeiou':
			new += 'way'
		else:
			new += 'ay'
		count = len(str)
	count += 1

print(new)