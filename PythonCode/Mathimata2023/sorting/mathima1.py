

import random

import sys
sys.path.insert(0,"/home/giannisvidras/Documents/Μαθήματα Python/Python-Code/PythonCode/Mathimata2023")

from functions import *
students = ["Δημήτρης" , "Ευγενία", "Ναταλία","Γιαννης", "Ρένια", "Αλεξανδρός"]
print(students)
students = bubble_sort(students)
print(students)

mylist = [5,4,3,2,1]

"""
for i in range(5):
    a = random.randint(1, 50)
    mylist.append(a)  
"""
print(mylist)
my_list_sorthed = bubble_sort(mylist)
print(my_list_sorthed)





