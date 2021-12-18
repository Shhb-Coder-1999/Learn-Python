def multiplication_table(user_choose):

    print('   ', end='')

    for i in range(0, user_choose):
        print(i+1 ,'  ', end='')
        
        
    print('  ')  

    for j in range(0, user_choose+1):
    
        print(" -" ,' ', end='')

    print('')        

    for i in range(0, user_choose):
        print(i+1 , ':', end='') 
        for j in range(0, user_choose):
            print((i+1)*(j+1) ,'  ', end='')
        print("\n")  


user_choose = int(input ("Please Enter col and row length :"))
multiplication_table(user_choose)

    