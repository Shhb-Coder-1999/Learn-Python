import random
import time
start = 0
end = 0
game = [['-','-','-'],
        ['-','-','-'],
        ['-','-','-']         
        ]
  
def printgame():
      for i in range(3):
            for j in range(3):
                print (game[i][j] , end=' ')   
            print()            

def print_result(user):
       print("----------------------------------------------")
       print(user ,"win !!")
       end = time.time()
       print ("your game time : " , end - start , "second")
       print("----------------------------------------------")

def check_game(user):
    

    counter = 0

    for i in range(3):
        for j in range(3):
         if   game[i][j] != '-' :
            counter = counter + 1;     

    if    (game[0][0] == "💚" and game[0][1] == "💚" and game[0][2] == "💚" ) :
       print_result('user1')
       return False   
    elif  (game[0][0] == "💙" and game[0][1] == "💙" and game[0][2] == "💙" ) :  
       print_result(user)
       return False   

    elif  (game[1][0] == "💚" and game[1][1] == "💚" and game[1][2] == "💚" ) :
       print_result('user1')
       return False   
    elif  (game[1][0] == "💙" and game[1][1] == "💙" and game[1][2] == "💙" ) :  
       print_result(user)
       return False   

    elif  (game[2][0] == "💚" and game[2][1] == "💚" and game[2][2] == "💚" ) :
       print_result('user1')
       return False      
    elif  (game[2][0] == "💙" and game[2][1] == "💙" and game[2][2] == "💙" ) :  
       print_result(user)
       return False    

    elif  (game[0][0] == "💚" and game[1][0] == "💚" and game[2][0] == "💚" ) :
            print_result('user1')
            return False    
    elif  (game[0][0] == "💙" and game[1][0] == "💙" and game[2][0] == "💙" ) :  
       print_result(user)
       return False   

    elif  (game[0][1] == "💚" and game[1][1] == "💚" and game[2][1] == "💚" ) :
       print_result('user1')
       return False   
    elif  (game[0][1] == "💙" and game[1][1] == "💙" and game[2][1] == "💙" ) :  
       print_result(user)
       return False   

    elif  (game[0][2] == "💚" and game[1][2] == "💚" and game[2][2] == "💚" ) :
           print_result('user1')
           
           return False      
    elif  (game[0][2] == "💙" and game[1][2] == "💙" and game[2][2] == "💙" ) :  
       print_result(user)
       return False   

    elif  (game[0][2] == "💚" and game[1][1] == "💚" and game[2][0] == "💚" ) :
            print_result('user1')
            
            return False     
    elif  (game[0][2] == "💙" and game[1][1] == "💙" and game[2][0] == "💙" ) :  
       print_result(user)
       return False    

    elif  (game[0][0] == "💚" and game[1][1] == "💚" and game[2][2] == "💚" ) :
            print_result('user1')
            
            return False     
    elif  (game[0][0] == "💙" and game[1][1] == "💙" and game[2][2] == "💙" ) :  
       print_result(user)
       return False    

    elif counter == 9 :
        print("----------------------------------------------")
        print("draw")
        print("----------------------------------------------")
        return False   
    else :
        return True 
        
                                    
def init_pc_choose():
    while check_game('pc') :
     random_pc_row = random.randint(0,2)
     random_pc_col = random.randint(0,2)

     if game[random_pc_row][random_pc_col] == '-':
         game[random_pc_row][random_pc_col] = '💙'
         break

    
def playwithpc():
    while check_game('pc'):
        while True :

            print("your color is green")
            user_row = int(input ("Please Enter row length :"))
            user_col = int(input ("Please Enter col length :"))

            if game[user_row-1][user_col-1] == '-':
                game[user_row-1][user_col-1] = "💚"
                init_pc_choose()
                printgame()
                break
            else :
                print("your choose isnt empty ! plz select another choose ...")
                printgame()



def twoplayers():
    
    while True:
        finish = 0
        while True :


            print("your color is green")
            user_row = int(input ("Please Enter row length :"))
            user_col = int(input ("Please Enter col length :"))

            if game[user_row-1][user_col-1] == '-':
                game[user_row-1][user_col-1] = "💚"
                printgame()
                if check_game('user2') == False :
                    finish = 'finish'
                break
            else :
                print("your choose isnt empty ! plz select another choose ...")
                printgame()
         

        if finish == 'finish':
             break    

        while True :
    
            print("your color is blue")
            user_row = int(input ("Please Enter row length :"))
            user_col = int(input ("Please Enter col length :"))

            if game[user_row-1][user_col-1] == '-':
                game[user_row-1][user_col-1] = "💙"
                printgame()
                if check_game('user2') == False :
                    finish = 'finish'
                break
            else :
                print("your choose isnt empty ! plz select another choose ...")
                printgame()  
 
        if finish == 'finish':
         break              



menu_options = {
    1: 'play with pc',
    2: 'play with another person',
    4: 'Exit',
}

def print_menu():
    for key in menu_options.keys():
        print (key, '--', menu_options[key] )

def option1():
     print('Handle option \'Option 1\'')

def option2():
     print('Handle option \'Option 2\'')


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
           game = [['-','-','-'],
                    ['-','-','-'],
                    ['-','-','-']         
                    ]
           start = time.time()
           playwithpc()

        elif option == 2:
            game = [['-','-','-'],
                    ['-','-','-'],
                    ['-','-','-']         
                    ]

            twoplayers()

        elif option == 4:
            print('Thanks message before exiting')
            exit()
        else:
            print('Invalid option. Please enter a number between 1 and 4.')