#sequential search over a random number....

import random
import timeit

start = 1 
end = 10000
step = 1
numForSearch = random.randint(start,end)
moves_counter = 0
flag = False

start_time = timeit.default_timer() 
for i in range(start, end, step):
    moves_counter += 1
    if(numForSearch == i):
        print("The number was ", numForSearch , "and was found in " , moves_counter)
        print("The range was between " , start , "to ", end)
        flag = True
        if(flag == True):
            break
end_time = timeit.default_timer()

execution_time = end_time - start_time
print("time tooked " ,execution_time)