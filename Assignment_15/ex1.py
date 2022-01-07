from math import *
def isSymmetric(list):
    for i in range(0, floor(len(list)/2)):
        if list[i] == list [len(list)-(i+1)]:
            continue
        else :
            return False
    return True        

list = []
n = int(input("Enter number of elements : "))
for i in range(0, n):
    ele = int(input())
    list.append(ele) 

if (isSymmetric(list)):
    print ("Yes")
else:
    print ("No")