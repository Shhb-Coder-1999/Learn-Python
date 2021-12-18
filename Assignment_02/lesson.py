
    # -------------------------------------Game-----------------------------------

import random
from typing import Counter

x = random.randint(0,20)
counter = 0

num =int(input ("please enter your number  :"))


while True:
    if num > x :
     counter += 1
     num = int (input ("your number is greather than result , enter again :"))
    elif num < x:
     counter += 1
     num = int (input ("your number is smaller than result , enter again :"))
    elif num == x:
        print ("you find number with" , counter , "try")
        break


    # ----------------------------------------------------------------------------





