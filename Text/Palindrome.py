str = input('Enter a string: ')
palin = ''

count = len(str) - 1

while count >= 0:
	palin += str[count]
	count -= 1

if str == palin:
	print(str, 'is a palindrome!')
else:
	print(str, 'is not a palindrome!')
