import datetime

def GetDate():
                   h= int(input('Plz enter hour :'))
                   m= int(input('Plz enter minustes :'))
                   s= int(input('Plz enter seconds :'))
                   return h , m , s

class Date:

    def __init__(self,time):
       self.time = time

    def add(self,time):
       fulldate = datetime.datetime(100, 1, 1, self.time.hour, self.time.minute, self.time.second)
       fulldate = fulldate + datetime.timedelta(seconds=time.time.second ,hours=time.time.hour , minutes=time.time.minute)
       return Date(fulldate)


    def sub(self,time):
       fulldate = datetime.datetime(100, 1, 1, self.time.hour, self.time.minute, self.time.second)
       fulldate = fulldate - datetime.timedelta(seconds=time.time.second ,hours=time.time.hour , minutes=time.time.minute)
       return Date(fulldate)

    def toDate(self):
        return Date(datetime.datetime.fromtimestamp(self.time)- datetime.timedelta(seconds=0 ,hours=3 , minutes=30))

    def toSec(self):
        return(Date(self.time.hour*3600 + self.time.minute*60 + self.time.second ))

    def __str__(self):
           if(isinstance(self.time, int)):
                  return f"{self.time}"
           else :       
            return f"{self.time.hour}:{self.time.minute}:{self.time.second}"   




    
def Menu():
       
        menu_options = {
        1: 'Add Two Date',
        2: 'Subtract Two Date',
        3: 'Seconds To Date',
        4: 'Date To Seconds',
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
                   print("------------first date----------")
                   h , m , s = GetDate()
                   d1 = Date(datetime.datetime(100,1,1,h,m,s))
                   print("------------first date----------")
                   h , m , s = GetDate()
                   d2 = Date(datetime.datetime(100,1,1,h,m,s))
                   print(d1.add(d2))

                elif option == 2:
                   print("------------first date----------")
                   
                   d1 = Date(datetime.datetime(100,1,1,h,m,s))
                   print("------------first date----------")
                   h , m , s = GetDate()
                   d2 = Date(datetime.datetime(100,1,1,h,m,s))
                   print(d1.sub(d2))
                     

                elif option == 3:
                        s= int(input('Plz enter seconds :'))
                        d1 = Date(s)
                        print(d1.toDate())
                     

                elif option == 4: 
                   h , m , s = GetDate()
                   d1 = Date(datetime.datetime(100,1,1,h,m,s))
                   print(d1.toSec())
                     

                elif option == 0:
                       print('Thanks message before exiting')
                       exit()
                else:
                    print('Invalid option. Please enter a number between 1 and 4.')        

Menu()






