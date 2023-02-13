string = "1 2 3 4 5 6 7 8 9 10"
list = [int(n) for n in string.split(" ")]

def rotate_right(list,k):
    for i in range(k):
        pop = list.pop()
        list.insert(0,pop)
    return list

string = input("Enter the string(num): ")
list = [int(n) for n in string.split(" ")]
k = int(input("Enter the no of positions to rotate: "))
print("\nRotated list: ",rotate_right(list,k))
tup = tuple([x for x in list])
print("Tuple:",tup)