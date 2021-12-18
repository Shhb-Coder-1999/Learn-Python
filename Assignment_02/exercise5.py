import math
print("Convert To Time")    
print("-----------------------------")

Time = int(input ("Please Enter Your Time (example = 3430) :"))

hour = Time / 3600 
min = (Time % 3600) / 60
second = (Time % 3600) % 60

print(math.floor(hour) ,":" , math.floor(min),":",math.floor(second))