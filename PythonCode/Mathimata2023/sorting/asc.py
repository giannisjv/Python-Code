def binarySearch( array, key ) :
    first = 0
    last = len(array) - 1
    found = False
    while (first <= last and not found):
        mid = ( first + last ) / 2
        mid = int(mid)
        if (array[ mid ] == key) :
            found = True
        elif (array[ mid ] < key):
            first = mid + 1
        else :
            last = mid - 1
    return found

mylist = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 15, 16]

a = int(input("num"))
print(binarySearch(mylist, a))

