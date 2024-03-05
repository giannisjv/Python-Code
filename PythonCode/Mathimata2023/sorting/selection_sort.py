
import random 
mylist = list()

for i in range(10):
    a = random.randint(1,50)
    mylist.append(a)

print(mylist)
for i in range(len(mylist)):
    min = i
    for j in range(i+1, len(mylist)):
        if(mylist[min] < mylist[j]):
            min = j

    temp = mylist[i]
    mylist[i] = mylist[min]
    mylist[min] = temp

print("\nsorted list\n")
for i in range(len(mylist)):
    print("%d" %mylist[i], end=" ")
print("\n")