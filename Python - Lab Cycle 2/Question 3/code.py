import json

file = open('iris.json','r')

irislines = file.readlines()
file.close()
for i in irislines: