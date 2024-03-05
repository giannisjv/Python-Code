# function 1 zhtao apo to xristi dedomena

def data(brand_list, value_list, mileage_list):
    br = input("Give The brand of your car ")
    brand_list.append(br)

    va = input("Give The value of your car ")
    value_list.append(va)
    
    km = input("Give The mileage of your car ")
    mileage_list.append(km)


def bubble_sort(list):
    N = len(list)
    for i in range(N-1):
        for j in range(N-1, i, -1):
            if(list[j] < list[j-1]):
                list[j], list[j-1] = list[j-1], list[j]
                print(j ,j-1)


# binary search function
def Binary_search(list, numForSearch):
    flag = False
    minNum = list[0]
    N = len(list)
    maxNum = N - 1
    while(flag == False):
        binaryNum = (minNum + maxNum) / 2
        binaryNum = int(binaryNum)
        if(numForSearch < list[binaryNum]):
            maxNum = binaryNum - 1

        elif(numForSearch > list[binaryNum]):
            minNum = binaryNum + 1
    
        elif(numForSearch == list[binaryNum]):
            flag = True
            print("found it")

# unsorted search function
def unsorted_list(list, numberForSearch):
    flag = False
    for i in range(len(list)):
        if(numberForSearch == list[i]):
            flag = True
            place = i
        else:
            flag = False
    if(flag == True):
        print("The number was ", numberForSearch , "It was found at ", place)
        print("The range was between " , 0 , "to ", len(list - 1))
    else:
         print("Did not found")      

# function to check if the list is sorted and make decide which search to use 
def is_sorted(list, numberForSearch):
    flag = False
    for i in range(len(list)):
        if(list[i - 1] > list[i]):
            flag = True
            break
        else:
            flag = False
    if(flag == True):
        unsorted_list(list, numberForSearch)
    else:
        Binary_search(list, numberForSearch)



brand_list = list()
value_list = list()
mileage_list = list()


exit = 0
while (exit != -1):
    choice = input("what to do\n1.insert data\n2. search\n 3. sort data")
    if(choice == 1):
        data(brand_list, value_list, mileage_list)
    
    
    print(brand_list, value_list, mileage_list)

bubble_sort(brand_list)
bubble_sort(value_list)