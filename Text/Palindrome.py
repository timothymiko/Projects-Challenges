str = input('Enter a string: ')
pal = ''

count = len(str) - 1

while count >= 0:
	pal += str[count]
	count -= 1

if str == pal:
	print(str, 'is a palindrome!')
else:
	print(str, 'is not a palindrome!')