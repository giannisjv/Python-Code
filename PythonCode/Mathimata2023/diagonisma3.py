def pyth():
    from math import sqrt, pi
    a = int(input("Give a"))
    b = int(input("Give b"))
    c = sqrt(a**2 + b**2)
    return c

def emvadon():
    import math
    r = int(input("Give r"))
    circ = 2 * math.pi * r**2
    return circ

a = "exit"
file_object = open("calc.txt", "r+")
while(a != "exit"):
    a = input("Επέλεξε μία πράξη")
    if(a == "emvadon"):
        result = emvadon()
        file_object.write(result, "\n")
    elif(a == "pyth"):
        result = pyth()
        file_object.write(result, "/n")
    elif(a == "exit"):
        print("Bye")