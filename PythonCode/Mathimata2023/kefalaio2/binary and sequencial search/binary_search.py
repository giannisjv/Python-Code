#binary search over a random number....

import random
import timeit

start = 1 
end = 100000
step = 1
#numForSearch = random.randint(start,end)
numForSearch = 89000
moves_counter = 0
flag = False
minNum = start
maxNum = end


start_time = timeit.default_timer() 

while(flag == False):
    moves_counter += 1
    binaryNum = (minNum + maxNum) / 2
    binaryNum = int(binaryNum)

    if(numForSearch < binaryNum):
        maxNum = binaryNum - 1

    elif(numForSearch > binaryNum):
        minNum = binaryNum + 1
   
    elif(numForSearch == binaryNum):
        print("The number was ", numForSearch , "and was found in " , moves_counter , "tries")
        print("The range was between " , start , "to ", end)
        flag = True

end_time = timeit.default_timer()

execution_time = end_time - start_time
print("time tooked " ,execution_time)