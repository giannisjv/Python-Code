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


x = IsGreatOrless(6,6)
print(x)
print(type(x))

def dym2(a):
  x = 1
  for i in range(a):
      x *= 2 
      print(x)