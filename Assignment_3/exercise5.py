user_choose = input ("Please Enter Your Number :")
numlist = list(user_choose) 

armstrong_num = 0

for i in range(0, len(numlist)):
    armstrong_num = armstrong_num + (int(numlist[i])**len(numlist))

if armstrong_num == int(user_choose):
    print("Yes")
else :
    print("No")    

