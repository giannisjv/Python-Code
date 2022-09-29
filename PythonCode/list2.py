thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
if "apple" in thislist:
  print("Yes, 'apple' is in the fruits list") 

newListWithA = []
newListWithB = [x for x in thislist if "b" not in x]
for x in thislist:
  if "a" in x and len(x) > 5:
    newListWithA.append(x)

print(newListWithA)
print(newListWithB)
new_list = [x for x in range(len(thislist))]

print(new_list)

thislist.append("Watermelon")
print(thislist)

thislist.sort(reverse=False, key=str.lower)
print(thislist)
