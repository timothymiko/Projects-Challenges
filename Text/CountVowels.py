str = input("Enter a new string: ")

count = 0
vowels = 0

a = 0
e = 0
i = 0
o = 0
u = 0

while count < len(str):
	if str[count] in 'aeiou':
		vowels += 1
		if str[count] in 'a':
			a += 1
		if str[count] in 'e':
			e += 1
		if str[count] in 'i':
			i += 1
		if str[count] in 'o':
			o += 1
		if str[count] in 'u':
			u += 1
	count += 1
	
print("Vowels: ", vowels)
print('A: ',a)
print("E: ", e)
print("I: ", i)
print("O: ", o)
print("U: ", u)
