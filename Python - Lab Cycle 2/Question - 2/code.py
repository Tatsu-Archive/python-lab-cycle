string = "1 2 3 4 5 6 7 8 9 10"
list = [int(n) for n in string.split(" ")]

def rotate_right(list,k):
    for i in range(k):
        pop = list.pop()
        list.insert(0,pop)
    return list

def tuple_list(list):
    return tuple([x for x in list])

def dup_list(tup):
    duptup =  tuple(set(tup))
    return list(duptup)

string = input("Enter the string(num): ")
list = [int(n) for n in string.split(" ")]
k = int(input("Enter the no of positions to rotate: "))
print("\nRotated list: ",rotate_right(list,k))

tup = tuple_list(list)
print("\nTuple:",tup)

print("\nDuplicates Removed List: ",dup_list(tup))