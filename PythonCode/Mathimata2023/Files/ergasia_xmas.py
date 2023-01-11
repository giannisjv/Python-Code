def IsExisting(path):
	import os
	exists = os.path.exists(path)
	return exists

anwser = "a"
while(anwser != "exit"):
    anwser = input("\n1. Δημιουργία αρχείου\n2. Άνοιγμα αρχείου (Read-only)\n3. Άνοιγμα Αρχείου(Write-Only)\n4. Άνοιγμα αρχείου(Read - Write)\nexit για τέλος: ")
    if (anwser == "1"):
        file_name = input("Δώσε το Όνομα του μαθητή: ")
        path = input("Πού θα ανοιχθεί το αρχείο; ")
        file = file_name + ".txt"
        file_name1 = path + "/" + file


        if(IsExisting(file_name) == False):
            print("Δημιουργία αρχείου", file_name1)
            fileObj = open(file_name1, "w")
            fileObj.write("Mathima\tVathmos")
            insert = "yes" 

            while(insert == "yes"):
                mathima = input("Εισαγωγή μαθήματος: ")
                Vathmos = float(input("Δώσε τον αριθμό από το 1 έως το 20: "))
                
                while(Vathmos < 1 or Vathmos > 20):
                    Vathmos = float(input("Δώσε τον αριθμό από το 1 έως το 20: "))
                fileObj.write(mathima + "\t" + str(Vathmos))
                insert = input("θέλεις να δώσεις και άλλο μάθημα; yes | no")
            fileObj.close()

        elif(IsExisting(file_name) == True):
            print("Το Αρχείο" + file_name1 + "υπάρχει")
            print("Τα δεδομένα ειναι:")
            fileObj = open(file_name1, "r")
            print(fileObj.read())
            print("Κλείσιμο αρχείου")
            fileObj.close()
    elif(anwser == "2"):
        file_name = input("Δώσε το Όνομα του μαθητή")
        path = input("Πού θα ανοιχθεί το αρχείο;")
        file = file_name + ".txt"
        file_name1 = path + "/" + file
