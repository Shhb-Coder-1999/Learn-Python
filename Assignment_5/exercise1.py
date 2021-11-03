import csv  

class Shop:

    products = [] 
    User_Bill = []
  

    def __init__(self):
        #  load product
         self._name = name
           
      
    # getter method
    def get_products(self):
        return self.products

    def get_User_Bill(self):
        return self.User_Bill


    # setter method
    def get_products(self, x):
        self.products = x

    def get_User_Bill(self, x):
        self.User_Bill = x

    @classmethod   

    def Add_New_Product (self , name , id , price , amount):
        self.products.append({"name":name , "id":id , "price":price , "amount":amount   })

    def Remove_Product (self , product_index):
        self.products.pop(product_index)  
              

    def Show_Products_List(self) :
        print("--------Products List-------")
        print("Number |" , "Name |" , "Id |" , "Price |" ,"Amount")
        print("-------------------------------------------------")
        counter = 1
        for product in self.products :
            print(counter , product.name , product.id, product.price ,product.amount)
            counter +=1
            print("-------------------------------------------------")

    def Edit_Product(self , index , param) :
        if (param == 'id') :
           self.products[index].id = param  
        elif(param == 'name') : 
           self.products[index].name = param 
        elif(param == 'amount') : 
           self.products[index].amount = param     
        elif(param == 'price') : 
           self.products[index].price = param  

    def Search_Product(self , SearchInput) :
         counter = 0 
         for product in self.products :
             if SearchInput in product: 
                print("-------Product Details-------")
                print("Name :",product.name)
                print("Price :",product.price)
                print("Id :",product.id)
                print("Amount :",product.amount)
                print("-----------------------------")
             else :
                 counter += 1
         if(counter == len(self.products) ) :
             print ("Couldn't Find This product !!!!") 
             print("-----------------------------") 

    def Bill(self , product_index ,amount) :
        self.User_Bill.append({"product" : self.products[product_index].name , "amount":amount})

    def Show_Bill(self)   :
        sum = 0 ;
        amount = 0;
        print("----------Your Bill----------")
        print("Name |" , "Id |" , "Price |" ,"Amount")
        for item in self.User_Bill :
             print(item.product.name , item.product.id, item.product.price ,item.amount)
             amount += item.amount
             sum += item.product.price*item.amount
        print("amount : " + amount , "Total : " + sum) 

    def Menu(self):
       
        menu_options = {
        1: 'Show_Products_List',
        2: 'Add_New_Product',
        3: 'Remove_Product',
        4: 'Edit_Product',
        5: 'Search_Product',
        6: 'Buy Product ',
        7: 'Show Bill',
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
                
                #Check what choice was entered and act accordingly
                if option == 1:
                
                    self.Show_Products_List()

                elif option == 2:
                    id = int(input('Enter your product id: '))
                    name = input('Enter your product number: ')
                    price = int(input('Enter your product number: '))
                    amount = int(input('Enter your product number: '))
                    self.Add_New_Product(name , id , price , amount)
                    print("--------Done----------")

                elif option == 3:
                   
                    number = int(input('Enter your product number: '))
                    if len(self.products)>number and number>0 :
                        self.Remove_Product(number) 
                        print("--------Done----------") 
                    else:
                        print("out of range!!!")

                elif option == 4: 
                    number = int(input('Enter your product number: '))
                    paramnum = int(input('Select your option :' , "1-name" , "2-id" , "3-amount" , "4-price"))
                    if paramnum == 1 :
                        self.Edit_Product(number , 'name' )
                        print("--------Done----------") 
                    elif paramnum == 2 : 
                        self.Edit_Product(number , 'id' )
                        print("--------Done----------") 
                    elif paramnum == 3 : 
                        self.Edit_Product(number , 'amount' )
                        print("--------Done----------") 
                    elif paramnum == 4 : 
                        self.Edit_Product(number , 'price' ) 
                        print("--------Done----------") 

                elif option == 5:   
                    searchinput= input('Enter your product number: ') 
                    self.Search_Product(searchinput)    
                    print("--------Done----------")  

                elif option == 6:    
                      number = int(input('Enter your product number: '))
                      if len(self.products)>number and number>0 :
                          amount = int(input('Enter your product amount: '))
                          if self.products[number].amount > amount :
                              self.Bill(number ,amount)
                              self.products[number].amount -+ amount
                              print("--------Done----------") 
                          else :
                              print("out of range of our product amount!!!") 

                    
                      else:
                            print("out of range!!!")  

                elif option == 7:
                    self.Show_Bill  
                    print("--------Done----------") 
        
                    
                    


                elif option == 0:
                    print('Thanks message before exiting')
                    exit()
                else:
                    print('Invalid option. Please enter a number between 1 and 4.')        



                      



             

    
            

            
            
        
        
         
        



