import math
from math import sqrt

def Get_Complex_Number():
    real = int(input('Plz enter real part of number :'))
    image = int(input('Plz enter image part of number :'))
    return real, image

class Complex(object):

    def __init__(self, real, imag=0.0):
        self.real = real
        self.imag = imag

    def __add__(self, other):
        return Complex(self.real + other.real, self.imag + other.imag)

    def __sub__(self, other):
        return Complex(self.real - other.real, self.imag - other.imag)
    
    def __mul__(self, other):
        return Complex((self.real * other.real) - (self.imag * other.imag),
            (self.imag * other.real) + (self.real * other.imag)) 

    def __str__(self):
        Str=""
        if(self.imag<0):
            Str=f"{self.imag}"
        elif self.imag==0:
            Str=""
        else:
            Str=f"+ {self.imag}"
        return str(self.real)+Str         

    
def Menu():
       
        menu_options = {
        1: 'Add Two Complex Numbers',
        2: 'Multiply  Two Complex Numbers',
        3: 'Subtract Two Complex Numbers',
        0: 'Exit',
            }

        def print_menu():
            for key in menu_options.keys():
                print (key, '--', menu_options[key] )

        if __name__=='__main__':
            while(True):
                print_menu()
                option = ''
                try:
                    option = int(input('Enter your choice: '))
                except:
                    print('Wrong input. Please enter a number ...')
             
                if option == 1:
                     print("---------Fisrt number ----------")
                     r , i = Get_Complex_Number()
                     num1 = Complex(r, i)
                     print("---------second number ----------")
                     r , i = Get_Complex_Number()
                     num2 = Complex(r, i)
                     print("result : " , num1+num2)

                elif option == 2:
                     print("---------Fisrt number ----------")
                     r , i = Get_Complex_Number()
                     num1 = Complex(r , i)
                     print("---------second number ----------")
                     r , i = Get_Complex_Number()
                     num2 = Complex(r , i)
                     print("result : " , num1*num2)

                elif option == 3:
                     print("---------Fisrt number ----------")
                     r , i = Get_Complex_Number()
                     num1 = Complex(r , i)
                     print("---------second number ----------")
                     r , i = Get_Complex_Number()
                     num2 = Complex(r , i)
                     print("result : " , num1-num2)
                elif option == 0:
                       print('Thanks message before exiting')
                       exit()
                else:
                    print('Invalid option. Please enter a number between 1 and 4.')        

Menu()
