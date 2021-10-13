import math

print ("-----------------------------------------------------------------------")
print ("please enter your expression : (example 1+2 or sin30) ")
print ("-----------------------------------------------------------------------")

while True:
    expression = input ()
    expression = expression.replace(" ", "")
    
    if expression.find('+') == True:
        result = expression.split('+')
        print (float(result [0]),"+", float(result[1]) , "=" , float(result[1]) + float(result [0]))
        print ("------------------------------")

    elif expression.find('-')==True:   
        result = expression.split('-')
        print (float(result [0]),"-", float(result[1]) , "=" , float(result[0]) - float(result [1]))
        print ("------------------------------")

    elif expression.find('/')==True:   
        result = expression.split('/')
        print (float(result [0]),"/", float(result[1]) , "=" , float(result[0]) / float(result [1]))
        print ("------------------------------")

    elif expression.find("sin") == 0:  
        result = expression.split("sin")
        print (math.sin(math.radians(float(result[1]))))
        print ("------------------------------")  

    elif expression.find("cos") == 0:  
        result = expression.split("cos")
        print (math.cos(math.radians(float(result[1]))))
        print ("------------------------------")  

    elif expression.find("tan") == 0:  
        result = expression.split("tan")
        print (math.tan(math.radians(float(result[1]))))
        print ("------------------------------")  

    elif expression.find("cot") == 0:  
        result = expression.split("cot")
        print (math.sin(1/math.radians(float(result[1]))))
        print ("------------------------------")  

    elif expression.find("log") == 0:  
        result = expression.split("log")
        print (math.log(float(result[1])))
        print ("------------------------------")                
