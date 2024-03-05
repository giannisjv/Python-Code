print("\n\n")
count = 0
cfor = True
cwhile = True
x = 2
print("      x\t\t k\t\t Για\t\t ΟΣΟ\t\t z\t\t Οθόνη\n")
for k in range(1, 10, 3):
    count += 1
    x = x + k
    print(" ",count,end = ".  ")
    count += 1
    print(x)
    
    print(" ",count,end = ".  ")
    count += 1
    print("\t\t",k)
    
    print(" ",count,end = ".  ")
    count += 1
    print("\t\t\t\t",cfor)
    z = 7

    print(" ",count,end = ".  ")
    count += 1
    print("\t\t\t\t\t\t\t\t",z)
    while(z < x):
        z = z + 2
        
        print(" ",count,end = ".  ")
        count += 1
        print("\t\t\t\t\t\t",cwhile)
        
        print(" ",count,end = ".  ")
        count += 1
        print("\t\t\t\t\t\t\t\t\t\t",z)
    
    print(" ",count,end = ".  ")
    count += 1
    print("\t\t\t\t\t\t\t\t\t\t",x)
print("\n\n")