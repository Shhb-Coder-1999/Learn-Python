import random

def rock_paper_scissors(user_choose):
    
    random_pc_choose = 0
    random_pc_choose = random.randint(1,3)
    result = 0


    # number 1 means pc choose rock 
    if   random_pc_choose == 1:
         print("<< pc choose rock >>")
         if   user_choose == 1:
            result  = 0
            return result
         elif user_choose == 2:
             result  = 1
             return result
         elif user_choose == 3:
            result  = 0
            return result
    # number 1 means pc choose paper
    elif  random_pc_choose == 2:
         print("<< pc choose paper >>")
         if   user_choose == 1:
            result=0
            return result
         elif user_choose == 2:
            result=0
            return result
         elif user_choose == 3:
            result=1
            return result 

    # number 1 means pc choose scissors
    elif  random_pc_choose == 3:
         print("<< pc choose scissors >>")
         if   user_choose == 1:
            result=1
            return result
         elif user_choose == 2:
            result=0
            return result
         elif user_choose == 3:
            result=0
            return result     

user_score = 0
print ("----------------------------------------")
print ("rock paper scissors Game✋✌✊")
print ("----------------------------------------")
for i in range(0, 5):
    print ("         round",i+1 ,"          your score : ",user_score)
    print ("----------------------------------------")
    print ("1-rock")
    print ("2-paper")
    print ("3-scissors")
    user_choose = int(input ("Please Enter Your Number :"))
    user_score = user_score + rock_paper_scissors(user_choose)
    print ("----------------------------------------")


if user_score >= 3 :
    print("You win !!!")
    print ("----------------------------------------")
else  :
    print("You lose !!!")
    print ("----------------------------------------")  



    