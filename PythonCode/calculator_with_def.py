def add(a, b):
	return a + b
def sub(a, b):
	return a - b
def mult(a, b):
	return a * b
def div(a, b):
	return a / b

c = input("Press a key, Press # for exit: ")
while c != "#":
	a = input('Give a: ')
	b = input('Give b: ')
	a = int(a)
	b = int(b)
	print("\nWhat operation should I use???")
	print("add for Add,\nsub for subtract,\nmult for multiplication,\ndiv for division: ")
	op = input()

	if op == "add":
		result = add(a, b)
	elif op == "sub":
		result = sub(a, b)
	elif op == "mult":
		result = mult(a, b)
	elif op == "div":
		result = div(a, b)
	else:
		print("Don't try to outsmart me, you just cant!!!\n")
		break
	print("The result from the operation ", op , "is: ",result)
	c = input("\nPress a key to continue, Press # for exit: ")
