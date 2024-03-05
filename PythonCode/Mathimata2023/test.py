"""
txt = "Hello 565.543"
flag = 0
num = ""
for i in txt:
    if (i.isdigit() == True or i =="."):
        flag = 1
        if(flag == 1):
            num += i
    else:
        flag = 0
    
num = float(num)
print(num)
print(type(num))


x = int(input("Δώσε αριθμό:\t"))
if x > 0:
    print("θετικός")
else:
    print("Αρνητικός")
"""

mlist =[0, 2, 5, 15, -1, 32, 14]
min = 100
max = -100
for i in range(1,7,2):
    A = mlist[i]
    B = mlist[i + 1]
    if A < B:
        Lmin = A
        Lmax = B
    else:
        Lmin = B
        Lmax = A
    if Lmin < min:
        min = Lmin
    if Lmax > max:
        max = Lmax
    print(A,B,Lmin,Lmax,min,max)
D = max * min
print(D)