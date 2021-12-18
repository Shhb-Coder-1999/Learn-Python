def multiplication_table(user_row , user_col):

    for i in range(0, user_row):
      for j in range(0, user_col):
          if i % 2 == 0 :
            print('#', end='') 
            print('*', end='') 
          else : 
            print('*', end='') 
            print('#', end='') 

      print('')    

      


user_col = int(input ("Please Enter col length :"))
user_row = int(input ("Please Enter row length :"))

multiplication_table(user_row , user_col)
