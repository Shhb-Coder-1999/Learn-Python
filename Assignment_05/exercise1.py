import csv  

class Shop:

    products = [] 
    User_Bill = []
  
    def __init__(self):
        f = open('/media/shb/3C50BD1450BCD63C/programming/Github/Learn_Python/Assignment_5/database.csv', 'r')
        for row in f:
            detail = row[:-1].split(',')
            product = {'name': detail[0], 'id': detail[1], 'price': detail[3], 'amount': detail[2]}
            self.products.append(product)

    @classmethod   

    def Add_New_Product (self , name , id , price , amount):
        self.products.append({'name':name , "id":id , "price":price , "amount":amount })

    def Remove_Product (self , product_index):
        self.products.pop(product_index-1)              

    def Show_Products_List(self) :
        print("--------Products List-------")
        print("Number|" , "Name|" , "Id |" , "Price|" ,"Amount")
        print("-------------------------------------------------")
        counter = 1
        for product in self.products :
          
            print(counter,"    |" , product['name'],"|" , product['id'],"|" , product['price'] ,"|" ,product['amount'])
            counter +=1
            print("-------------------------------------------------")

    def Edit_Product(self , index , param ,paramnum ) :
        if (paramnum  == 2) :
           self.products[index]['id'] = param        
        elif(paramnum  == 1) : 
           self.products[index]['name'] = param 
        elif(paramnum  == 3) : 
           self.products[index]['amount'] = param     
        elif(paramnum  == 4) : 
           self.products[index]['price'] = param  

    def Search_Product(self , SearchInput) :
         counter = 0 
         for product in self.products :
             if SearchInput in product: 
                print("-------Product Details-------")
                print("Name :",product['name'])
                print("Price :",product['price'])
                print("Id :",product['id'])
                print("Amount :",product['amount'])
                print("-----------------------------")
             else :
                 counter += 1
         if(counter == len(self.products) ) :
             print ("Couldn't Find This product !!!!") 
             print("-----------------------------") 

    def Bill(self , product_index ,amount) :
        self.User_Bill.append({"name" : self.products[product_index]['name'] , "amount":amount, "price": self.products[product_index]['price']})

    def Show_Bill(self)   :

        sum = 0 ;
        amount = 0;
        print("----------Your Bill----------")
        print("Name |" , "Id |" , "Price |" ,"Amount")
        for item in self.User_Bill :
             amount += item['amount']
             sum += int(item['price'])*item['amount']
        print("amount : " , amount , "Total : "  , sum) 


    def Menu(self):
       
        menu_options = {
        1: 'Show_Products_List',
        2: 'Add_New_Product',
        3: 'Remove_Product',
        4: 'Edit_Product',
        5: 'Search_Product',
        6: 'Buy Product ',
        7: 'Show Bill',
        0: 'Save & Exit',
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
                
                    self.Show_Products_List()

                elif option == 2:
                    id = int(input('Enter your product id: '))
                    name = input('Enter your product name: ')
                    price = int(input('Enter your product price: '))
                    amount = int(input('Enter your product amount: '))
                    self.Add_New_Product(name , id , price , amount)
                    print("--------Done----------")

                elif option == 3:
                   
                    number = int(input('Enter your product number: '))
                    if len(self.products)>=number and number>0 :
                        self.Remove_Product(number) 
                        print("--------Done----------") 
                    else:
                        print("out of range!!!")

                elif option == 4: 
                    number = int(input('Enter your product number: '))
                    print('Select your option :' , "1-name" , "2-id" , "3-amount" , "4-price")
                    paramnum = int(input())
                    if paramnum == 1 :
                        name = input('Enter your new product name: ')
                        self.Edit_Product(number-1 , name , paramnum  )
                        print("--------Done----------") 
                    elif paramnum == 2 : 
                        id = int(input('Enter your new product id: '))
                        self.Edit_Product(number-1 , id , paramnum  )
                        print("--------Done----------") 
                    elif paramnum == 3 : 
                        amount = int(input('Enter your new product amount: '))
                        self.Edit_Product(number-1 , amount ,paramnum  )
                        print("--------Done----------") 
                    elif paramnum == 4 : 
                        price = int(input('Enter your new product price: '))
                        self.Edit_Product(number-1 , price ,paramnum  ) 
                        print("--------Done----------") 

                elif option == 5:   
                    searchinput= input('Enter your product name: ') 
                    self.Search_Product(searchinput)    
                    print("--------Done----------")  

                elif option == 6:    
                      number = int(input('Enter your product number: '))                         
                      if len(self.products)>=number and number>0 :
                          
                          amount = int(input('Enter your product amount: ')) 

                          if int(self.products[number-1]['amount'])> amount :
                              self.Bill(number-1 ,amount)
                              after_amount =int(self.products[number-1]['amount']) 
                              after_amount-= amount
                              self.products[number-1]['amount']=after_amount
                              print("--------Done----------") 
                          else :
                              print("out of range of our product amount!!!") 

                    
                      else:
                            print("out of range!!!")  

                elif option == 7:
                    self.Show_Bill()  
                    print("--------Done----------") 
        
                    

                elif option == 0:
                    
                       a_file = open("/media/shb/3C50BD1450BCD63C/programming/Github/Learn_Python/Assignment_5/database.csv", "w")
                       arr = []
                       for item in self.products:

                            writer = csv.writer(a_file)
                            for key, value in item.items():
                                arr.append(value)

                           
                            writer.writerow(arr)    
                            arr = []    
                                    

                       a_file.close()
                       print('Thanks message before exiting')
                       exit()
                else:
                    print('Invalid option. Please enter a number between 1 and 4.')        


new_shop = Shop()
new_shop.Menu()
                      



             

    
            

            
            
        
        
         
        



