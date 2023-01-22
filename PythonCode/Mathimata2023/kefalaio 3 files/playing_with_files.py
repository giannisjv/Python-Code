
def IsAlive(path):
    import os
    alive = os.path.exists(path)
    return alive

path = "/home/giannisvidras/Documents/Μαθήματα Python/Python-Code/newfile.txt"
Alive = IsAlive(path)
counter = 0

if(IsAlive(path) == True):
    myfile = open("newfile.txt", "r")
    #print(myfile.read())

    for i in myfile.readlines():
        counter += 1
    print(counter)
    myfile.close()
elif(Alive == False):
    myfile = open("newfile.txt", "w")
    myfile.write("This is the first line")
    myfile.close
