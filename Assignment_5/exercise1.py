import csv  

class Shop:

    products = [] 
    User_Bill = []
  

    def __init__(self, name = 0 , id = 0  , price = 0 , amount = 0 ):
         self._name = name
         self._price = price
         self._amount = amount
         self._id = id    

      
    # getter method
    def get_name(self):
        return self._name

    def get_price(self):
        return self._price

    def get_id(self):
        return self._id        

    def get_amount(self):
        return self._amount

    # setter method
    def get_name(self, x):
        self._name = x

    def get_price(self, x):
        self._price = x

    def get_id(self, x):
        self._id = x      

    def get_amount(self, x):
        self._amount = x  

    #methods    

    def Show_Products_List(self) :
        print("--------Products List-------")
        print("Number |" , "Name |" , "Id |" , "Price |" ,"Amount")
        print("-------------------------------------------------")
        counter = 1
        for product in self.products :
            print(counter , product.name , product.id, product.price ,product.amount)
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



             

    
            

            
            
        
        
         
        



