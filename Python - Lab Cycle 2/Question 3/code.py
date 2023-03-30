'''Read the file 'iris.json' as a text file :
1. Create a list having each line of the file as an element
2. Convert it into a list of dictionary objects.
3. Show the details of all flowers whose species is
"setosa".
4. Print the minimum petal area and max sepal area in
each species
5. Sort the list of dictionaries according to the total area
are sepal and petal.
'''

import json
import math

with open('iris.json', 'r') as f:
    data = f.readlines()



def printall():
    print('Details of all flowers whose species is "setosa"')
    for i in data:
        if i['species'] == 'setosa':
            print(i)

def printminmax():
    print('Minimum petal area and max sepal area in each species')
    for i in data:
        print('Species: ', i['species'])
        print('Minimum petal area: ', min([math.pi*j['petal length']*j['petal width'] for j in data if j['species'] == i['species']]))
        print('Maximum sepal area: ', max([math.pi*j['sepal length']*j['sepal width'] for j in data if j['species'] == i['species']]))
        print()
            
def printsort():
    print('Sort the list of dictionaries according to the total area are sepal and petal')
    data.sort(key = lambda x: math.pi*x['petal length']*x['petal width'] + math.pi*x['sepal length']*x['sepal width'])
    print(data)

print("MENU DRIVEN PROGRAM")
print("1. Show the details of all flowers whose species is setosa")
print("2. Print the minimum petal area and max sepal area in each species")
print("3. Sort the list of dictionaries according to the total area are sepal and petal")
print("4. Exit")
while True:
    choice = int(input("Enter your choice: "))
    if choice == 1:
        printall()
    elif choice == 2:
        printminmax()
    elif choice == 3:
        printsort()
    elif choice == 4:
        break
    else:
        print("Invalid choice")
    