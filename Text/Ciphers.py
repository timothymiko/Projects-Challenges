import random

str = input('Please input a string: ')
str = str.upper()
alpha = [ 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 
	'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z' ]

# Caesar Cipher
caesar = ''

for c in str:
	if (alpha.index(c) + 5) > 25:
		shift = alpha.index(c) - 21
	else:
		shift = alpha.index(c) + 5
	caesar += alpha[shift]
	
# Vigenere Cipher
vigenere = ''
key = 'TIMOTHY' #19-8-12-14-19-7-24
count = 0

for c in str:
	if count > 6:
		count = 0
	shift = alpha.index(c) + alpha.index(key[count])
	if shift > 25:
		shift -= 26
	vigenere += alpha[shift]
	count += 1
	
# Vernam (One-Time Pad) Cipher
vernam = ''
otp = ''
count = 0

for c in str:
	otp += alpha[random.randint(0, 25)]
for c in str:
	shift = alpha.index(c) + alpha.index(otp[count])
	if shift > 25:
		shift -= 26
	vernam += alpha[shift]
	count += 1

print('\nInput: %s' % str)
print('Caesar: %s' % caesar)
print('Vigenere: %s' % vigenere)
print('Vernam: %s' % vernam)
print('One-Time Pad: %s' % otp)
