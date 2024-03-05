#sequential search over a random number....

import random
import timeit

start = 1 
end = 100000
#numForSearch = random.randint(start,end)
numForSearch = 89000
moves_counter = 0
flag = False
i=0

start_time = timeit.default_timer() 
while(start <= end and not flag):
    moves_counter += 1
    if(numForSearch == i):
        print("The number was ", numForSearch , "and was found in " , moves_counter)
        print("The range was between " , start , "to ", end)
        flag = True
    else:
        i += 1
end_time = timeit.default_timer()

execution_time = end_time - start_time
print("time tooked " ,execution_time)