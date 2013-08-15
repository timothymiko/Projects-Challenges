input = input('Enter your word: ')

words = input.split()
nwords = []
new = ''

for str in words:
	count = 0
	firstVow = 0
	num = 0
	while count < len(str):
		if str[count] in 'aeiouy':
			new = ''	
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
			nwords.append(new)
		count += 1
		
print(' '.join(nwords))
