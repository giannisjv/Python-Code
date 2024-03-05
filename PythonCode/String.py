from ast import BitAnd


brand = "Renault"
model = "Megane"
price = 1700

myCar = "My car was made by {1}, The model is {0}, And i bought it for {2} euros"

print(myCar.format(model, brand, price + 200))

print(myCar.isidentifier())

print(bool("hello"))

def myFuc():
    x = 6.6
    return x  

if myFuc():
    print(isinstance(myFuc(), int))
else:
    print("You can\'t find me!")

x = 5
y = x << 1
print(y)

def my_bin(x):
    bit = ''
    while x:
        bit += str(x % 2)
        x >>= 1
    return '0' + bit[::-1]

print(my_bin(10))
print(my_bin(6))

x = y = "5"

print(x in y) 

print(10 & 20 )

print(10 | 4)