from os import listdir


myList = []
x = input("Δώσε ένα στοιχείο, # για έξοδο. ")
while x != "#":
 myList.append(x)
 x = input("Δώσε ένα στοιχείο, # για έξοδο. ")
print(myList)
lilen = len(myList)
y = input("Διάλεξε από το 1 εως το: %d" %lilen)
y =+ 1
myList[y]
print(myList[y])
print(len(myList))

