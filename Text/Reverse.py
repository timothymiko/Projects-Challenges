str = input('Enter a string: ')
rev = ''

count = len(str) - 1

while count >= 0:
	rev += str[count]
	count -= 1
	
print('Reverse: ' + rev)