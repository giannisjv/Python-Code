def IsExisting(path):
	import os
	exists = os.path.exists(path)
	return exists

anwser = "a"
while(anwser != "exit"):
    anwser = input("\n1. Δημιουργία αρχείου\n2. Άνοιγμα αρχείου (Read-only)\n3. Προσθήκη στο αρχείο\n4. Εμφάνιση μόνο των βαθμών\nexit για τέλος: ")
    if (anwser == "1"):
        file_name = input("Δώσε το Όνομα του μαθητή: ")
        path = input("Πού θα ανοιχθεί το αρχείο; ")
        file = file_name + ".txt"
        file_name1 = path + "/" + file


        if(IsExisting(file_name1) == False):
            print("Δημιουργία αρχείου", file_name1)
            fileObj = open(file_name1, "w")
            fileObj.write("Mathima\tVathmos\n")
            insert = "yes" 

            while(insert == "yes"):
                mathima = input("Εισαγωγή μαθήματος: ")
                Vathmos = float(input("Δώσε τον αριθμό από το 1 έως το 20: "))
                
                while(Vathmos < 1 or Vathmos > 20):
                    Vathmos = float(input("Δώσε τον αριθμό από το 1 έως το 20: "))
                fileObj.write(mathima + "\t" + str(Vathmos) + "\n")
                insert = input("θέλεις να δώσεις και άλλο μάθημα; yes | no")
            fileObj.close()

        elif(IsExisting(file_name1) == True):
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
        
        fileObj = open(file_name1,"r")
        print(fileObj.read())
        fileObj.close()

    elif(anwser == "3"):
        file_name = input("Δώσε το Όνομα του μαθητή: ")
        path = input("Πού θα ανοιχθεί το αρχείο; ")
        file = file_name + ".txt"
        file_name1 = path + "/" + file

        if(IsExisting(file_name1) == True):
            fileObj = open(file_name1, "a")
            insert = "yes" 

            while(insert == "yes"):
                mathima = input("Εισαγωγή μαθήματος: ")
                Vathmos = float(input("Δώσε τον αριθμό από το 1 έως το 20: "))
                
                while(Vathmos < 1 or Vathmos > 20):
                    Vathmos = float(input("Δώσε τον αριθμό από το 1 έως το 20: "))
                fileObj.write(mathima + "\t" + str(Vathmos) +"\n")
                insert = input("θέλεις να δώσεις και άλλο μάθημα; yes | no")
            fileObj.close()
        elif(IsExisting(file_name1 == False)):
            fileObj = open(file_name1, "a")
            fileObj.write("Mathima\tVathmos")
            insert = "yes" 

            while(insert == "yes"):
                mathima = input("Εισαγωγή μαθήματος: ")
                Vathmos = float(input("Δώσε τον αριθμό από το 1 έως το 20: "))
                
                while(Vathmos < 1 or Vathmos > 20):
                    Vathmos = float(input("Δώσε τον αριθμό από το 1 έως το 20: "))
                fileObj.write(mathima + "\t" + str(Vathmos) + "\n")
                insert = input("θέλεις να δώσεις και άλλο μάθημα; yes | no")
            fileObj.close()
        
    elif(anwser == "4"):
            """
            file_name = input("Δώσε το Όνομα του μαθητή: ")
            path = input("Πού θα ανοιχθεί το αρχείο; ")
            file = file_name + ".txt"
            file_name1 = path + "/" + file
            """
            total = 0
            counter = 0
            fileObj = open("/home/giannisvidras/Documents/Python-Code/PythonCode/Mathimata2023/Files/Vidras.txt", "r")

            lines = fileObj.readlines()
            flag = 0
            num = ""
            for line in lines:
                for i in line:
                    if(i.isdigit() == True or i == "."):
                        flag = 1
                        if(flag == 1):
                            num += i
                    elif(i == "\n"):
                        print(num)
                        flag = 0
                        num = ""

    elif(anwser == "exit"):
        print("Goodbye")
    else:
        print("Wrong anwser you little redneck")

else:
            print("Wrong anwser you little redneck")

