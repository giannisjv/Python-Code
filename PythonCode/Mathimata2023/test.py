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
"""

x = int(input("Δώσε αριθμό:\t"))
if x > 0:
    print("θετικός")
else:
    print("Αρνητικός")