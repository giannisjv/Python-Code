from random import randint, random
from ssl import OP_NO_RENEGOTIATION
from typing import Counter


#Klasikoi Algotithmoi 

import random
def list_input(x, y):
    #print("Lista, antikeimeno")
    return x.append(y)
number = random.randint(1, 10)
counter = 0
mylist = list()

for i in range (1, 11):
    list_input(mylist, i)

#print(mylist)

for i in range(len(mylist)):
    if (number == i):
        counter += 1

if (counter != 0):
    print("O arithmos ", number, " vrethime " , counter , " fores")
