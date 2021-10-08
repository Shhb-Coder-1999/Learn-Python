import math

print ("please select your operestion /n")


print ("+ => sum")
print ("- => subtraction")
print ("/ => divide")
print ("* => multiplication")
print ("sin => sin")
print ("cos => cos")
print ("cot => cot")
print ("tan => tan")
print ("log => log")



height = input ()
print (float(height.split('+')[0].strip().replace(" ", "")) ,"+", float(height.split("+",1)[1].replace(" ", "")) , "=" , 4 )
