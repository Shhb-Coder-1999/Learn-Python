weight = float (input ("please enter your weight(kg)  :"))
height = float (input ("please enter your height(m)  :"))

BMI = weight / (height*height)

if   BMI<18.5 :
         print ("Your BMI :" , BMI)
         print ("underweight")

elif BMI>=18.5 and BMI<25   : 
         print ("Your BMI :" , BMI)
         print ("normal")
        
elif BMI>=25 and BMI<30   : 
         print ("Your BMI :" , BMI)
         print ("overweight")

elif BMI>=30 and BMI<35   : 
         print ("Your BMI :" , BMI)
         print ("overweight")

elif BMI>=35   : 
         print ("Your BMI :" , BMI)
         print ("overweight")
