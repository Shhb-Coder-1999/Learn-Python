import random

def calc(user_choose):

    random_pc_choose_1 = 0
    random_pc_choose_2 = 0
    random_pc_choose_1 = random.randint(1,2)
    random_pc_choose_2 = random.randint(1,2)
    print (user_choose)
    print(random_pc_choose_1)
    print(random_pc_choose_2)
    result = 0

    if (random_pc_choose_1 == 1 and random_pc_choose_2 == 1 and user_choose == 1 ) or (random_pc_choose_1 == 2 and random_pc_choose_2 == 2 and user_choose == 2) :
        result = -1
        return result

    elif ((random_pc_choose_1 == 1 and random_pc_choose_2 == 2 and user_choose == 2 ) or (random_pc_choose_1 == 2 and random_pc_choose_2 == 1 and user_choose == 1) ):
        result = 1
        return result

    elif (random_pc_choose_1 == 1 and random_pc_choose_2 == 2 and user_choose == 1 ) or (random_pc_choose_1 ==2  and random_pc_choose_2 == 1 and user_choose == 2) :
        result = 2
        return result 

    elif (random_pc_choose_1 == 2 and random_pc_choose_2 == 2 and user_choose == 1 ) or (random_pc_choose_1 ==1  and random_pc_choose_2 == 1 and user_choose == 2) :
        result = 3
        return result       

    










pc1_score = 0
pc2_score = 0
user_score = 0
print("--------------------------------------------")
print("Play Palam, Palam, Polish  ✋🤚")




for i in range(0, 5):
    print("--------------------------------------------")
    print ("round",i+1 ,"        your score : ",user_score  ,"| pc1 : ",pc1_score,"| pc2 : ",pc2_score )   
    print("--------------------------------------------")
    print("1 = ✋ ")
    print("2 = 🤚 ")
    user_choose = int(input ("Please Enter Your Option :"))
    result = calc(user_choose)
    if  result== 1 :
        pc1_score = pc1_score + 1
    elif  result == 2 : 
        pc2_score = pc2_score + 1 
    elif  result == 3 : 
        user_score = user_score + 1 


if   pc1_score > pc2_score and pc1_score > user_score    :
     print("--------------------------------------------")
     print ("your score : ",user_score  ,"| pc1 : ",pc1_score,"| pc2 : ",pc2_score ) 
     print("--------------------------------------------")   
     print ("pc 1 win !!!")  
elif pc2_score > pc1_score and pc2_score > user_score :  
     print("--------------------------------------------")
     print ("your score : ",user_score  ,"| pc1 : ",pc1_score,"| pc2 : ",pc2_score ) 
     print("--------------------------------------------")   
     print ("pc 2 win !!!")  
elif user_score > pc2_score and user_score > pc1_score  :  
     print("--------------------------------------------")
     print ("your score : ",user_score  ,"| pc1 : ",pc1_score,"| pc2 : ",pc2_score ) 
     print("--------------------------------------------")    
     print ("You win !!!")                
else :
    print("--------------------------------------------")
    print ("your score : ",user_score  ,"| pc1 : ",pc1_score,"| pc2 : ",pc2_score ) 
    print("--------------------------------------------")   
    print ("Tie !!!")          



