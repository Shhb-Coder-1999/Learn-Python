
user_choose = int(input ("How many number do you want to enter ? :"))
array = []

for i in range(0, user_choose):
    array.append( int(input ("please enter your number : ")))

sorted_array = sorted(array)


if array == sorted_array :
    print("yes")
else:
     print("no")   
