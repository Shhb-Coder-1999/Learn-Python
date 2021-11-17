def Get_Fractional_Number():
    numerator = int(input('Plz enter numerator of number :'))

    while True :
        denumerator = int(input('Plz enter denumerator of number :'))
        if denumerator != 0:
            break
        else :
            print("0 cant set as denumerator !!!! \n")

    return numerator , denumerator


class Fractional_Number :
    def __init__(self,numerator,denumerator):
        self.numerator=numerator
        self.denumerator=denumerator
        

    def __mul__(self,f_num) :
        numerator = (self.numerator * f_num.numerator )
        denumerator =(self.denumerator * f_num.denumerator)
        return Fractional_Number(numerator  , denumerator)


    def __add__(self,f_num) :   
        if(self.denumerator == f_num.denumerator):
            Fraction = self.numerator + f_num.numerator
            return Fractional_Number(Fraction , self.denumerator )
        else:
            Fraction = (self.numerator * f_num.denumerator) + (f_num.numerator * self.denumerator)
            return Fractional_Number(Fraction , self.denumerator * f_num.denumerator)

    def __sub__(self,f_num) :   
        if(self.denumerator == f_num.denumerator):
            Fraction = self.numerator - f_num.numerator
            return Fractional_Number(Fraction , self.denumerator )
        else:
            Fraction = (self.numerator * f_num.denumerator) - (f_num.numerator * self.denumerator)
            return Fractional_Number(Fraction , self.denumerator* f_num.denumerator)

    def __truediv__(self,f_num):
        numerator = (self.numerator * f_num.denumerator )
        denumerator =(self.denumerator * f_num.numerator)
        return Fractional_Number(numerator  , denumerator)

    def __str__(self):
        return  str(self.numerator)+ '/' + str(self.denumerator)    

    
def Menu():
       
        menu_options = {
        1: 'Add Two Fractional Numbers',
        2: 'Divide Two Fractional Numbers',
        3: 'Subtract Two Fractional Numbers',
        4: 'Multiply Two Fractional Numbers',
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
                     n1 , den1 = Get_Fractional_Number()
                     num1 = Fractional_Number(n1 , den1)
                     print("---------second number ----------")
                     n2 , den2 = Get_Fractional_Number()
                     num2 = Fractional_Number(n2 , den2)
                     print("result : " , num1+num2)

                elif option == 2:
                     print("---------Fisrt number ----------")
                     n1 , den1 = Get_Fractional_Number()
                     num1 = Fractional_Number(n1 , den1)
                     print("---------second number ----------")
                     n2 , den2 = Get_Fractional_Number()
                     num2 = Fractional_Number(n2 , den2)
                     print("result : " , num1/num2)

                elif option == 3:
                     print("---------Fisrt number ----------")
                     n1 , den1 = Get_Fractional_Number()
                     num1 = Fractional_Number(n1 , den1)
                     print("---------second number ----------")
                     n2 , den2 = Get_Fractional_Number()
                     num2 = Fractional_Number(n2 , den2)
                     print("result : " , num1-num2)

                elif option == 4: 
                     print("---------Fisrt number ----------")
                     n1 , den1 = Get_Fractional_Number()
                     num1 = Fractional_Number(n1 , den1)
                     print("---------second number ----------")
                     n2 , den2 = Get_Fractional_Number()
                     num2 = Fractional_Number(n2 , den2)
                     print("result : " , num1*num2)

                elif option == 0:
                       print('Thanks message before exiting')
                       exit()
                else:
                    print('Invalid option. Please enter a number between 1 and 4.')        

Menu()