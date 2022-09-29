#pythagoreio.py>
def My_pow(a):
   return a ** 2

def My_sum(a, b):
   return a + b 

def My_sqrt(a):
   import math
   return math.sqrt(a)
   
import string

count = 0   
a = input("Δώσε τον Α ή # για Έξοδο: ")

while(a != "#" and a != string.ascii_letters):
 count += 1
 print("Αυτό είναι ένα πρόγραμμα επίλυσης του πυθαγόρειου θεωρήματος")
 #a = input("Δώσε το Α:	")
 b = input("Δώσε το B:	")
 a = float(a)
 b = float(b)

 a = My_pow(a)
 b = My_pow(b)

 c = My_sum(a, b)
 c = My_sqrt(c)
 print("Η υποτείνουσα είναι: ", c)
 a = input("Δώσε τον Α ή # για Έξοδο: ")
print("Οι φορες που χρησιμοποιήθηκε το πρόγραμμα είναι (%d) " % count)
