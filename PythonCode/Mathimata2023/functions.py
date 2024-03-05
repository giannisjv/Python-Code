def IsEqual(x, y):
    if(x == y):
        return True
    else:
        return False

def add(x, y):
    return x + y

def IsDiffer(x, y):
    if(x == y):
        return False
    elif(x != y):
        return True 

def IsGreatOrless(x, y):
      if (x < y):
        return "x is greater than y"
      elif(x >y):
        return "y is greter than x"
      elif(IsEqual(x, y) == True):
        return "x and y are equal"

def pow2(a):
  x = 1
  for i in range(a):
      x *= 2 
      print(x)

def bubble_sort(array):
    N = len(array)
    for i in range(N-1):
        for j in range(N-1,i,-1):
            if (array[j] < array[j-1]):
                temp = array[j]
                array[j] = array[j-1]
                array[j-1] = temp
    return array