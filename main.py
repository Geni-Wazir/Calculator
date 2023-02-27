from add import addition
from subtract import subtract
from multiply import multiply
from divide import divide
from logarithm import logarithm
from power import power


print('''
	WELCOM TO nu

	1. Addition
	2. Subtraction
	3. Multiplication
	4. Division
	5. Log
	6. Power

	''')

ch = input("Your choice: ")

if ch == '5':
	a = float(input('Number: '))
	b = float(input('Base: '))
	print(logarithm(a,b))
elif ch == '6':
	a = float(input('Base: '))
	b = float(input('Power: '))
	print(power(a,b))
else:
	a = float(input('Number1 : '))
	b = float(input('Number2: '))
	if ch == '1':
		print(addition(a,b))
	elif ch == '2':
		print(subtract(a,b))
	elif ch == '3':
		print(multiply(a,b))
	elif ch == '4':
		print(divide(a,b))
	else:
		print("Choose only from the given option")





