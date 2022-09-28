max = 0
mo = 0
on = []
vath = []
sch = []
sch_var = input("Dose to School! ")
while(sch_var != "stop"):
 
 on1 = input("Dose onoma!")
 on.append(on1)
 
 vath2 = int(input("Dose vathmo! "))
 while vath2>100 or vath2<1:
   print("O arithmos einai ektos orion! ")
   vath2 = int(input("Dose vathmo! "))
 vath.append(vath2)
 mo += vath2
 
 print("stop gia exodo")
 sch_var = input("Dose to School! ")
 sch.append(sch_var)

print("O Mo einai: ",mo)

for i in vath:
 if i>max:
  max = i
  thesi = vath[i]
 
  
