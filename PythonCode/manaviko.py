def list_append(list, item):
	list.append(item)
	return list
	
def list_remove(list, item):
	list.remove(item)
	return list
	
def list_search(list, item):
	if item in list:
	  print("Το προιόν ", item , "βρέθηκε!")
	else:
	  print("Δεν βρέθηκε το προίον ",item)

def list_view(list):
	print (list)

def list_sort(list):
	list.sort()
	return list

mylist = []
print("\n\n")
print("Επέλεξε ένα από τα παρακάτω\n")
print("1 για πρόσθεση προιόντος στην λίστα\n")
print("2 για αφαίρεση προιόντος στην λίστα\n")
print("3 για αναζήτηση προιόντος στην λίστα\n")
print("4 για εμφάνιση της λίστας\n")
print("5 για ταξινόμηση της λίστας\n")
ans = input("exit για έξοδο!\n")

while ans != "exit":
   
	if ans == "1":
			item = input("Δώσε το προιόν που θέλεις να είσαγθει στην λίστα: ")
			list_append(mylist, item)
	elif ans == "2":
			if mylist:
			    item = input("Δώσε το προιόν που θέλεις να αφαιρεθεί από την λίστα: ")
			    list_remove(mylist, item)
			else:
			    print("Η λίστα είναι κενή, δεν υπάρχει κάτι για προς διαγραφή: ")
	elif ans == "3":
			if mylist:
			    search = input("Δώσε το προιόν που θέλεις προς αναζήτηση: ") ### "apple"
			    list_search(mylist, search)
			else:
			    print("Η λίστα είναι κενή, δεν υπάρχει κάτι για προς αναζήτηση: ")
	elif ans == "4":
			if mylist:
			    print(mylist)
			else:
			    print("Η λίστα είναι κενή, δεν υπάρχει κάτι για να δείξω: ")
	elif ans == "5":
			if mylist:
			    print("Η λίστα ταξινομημένη!")
			    list_sort(mylist)
			    print (mylist)
			else:
			    print("Η λίστα είναι κενή, δεν υπάρχει κάτι για να ταξινομηθεί!")
	print("\n\n")		    
	print("Επέλεξε ένα από τα παρακάτω\n")
	print("1 για πρόσθεση προιόντος στην λίστα\n")
	print("2 για αφαίρεση προιόντος στην λίστα\n")
	print("3 για αναζήτηση προιόντος στην λίστα\n")
	print("4 για εμφάνιση της λίστας\n")
	print("5 για πρόσθεση προιόντος στην λίστα\n")
	ans = input("exit για έξοδο!\n")
  
