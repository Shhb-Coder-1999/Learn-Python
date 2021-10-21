import random

subjects=["bacon","beef","chiken","duck","sausages","salmon","soap","pizza"]


selectedWord=subjects[random.randint(0,len(subjects)-1)]


chance=7
user_true_char=[]
while "true":
    win=1
    for anyChar in selectedWord:
        if anyChar in user_true_char:
            print(anyChar,end='')
        else:
            print("_ ",end='') 
            win=0
    if win==1:
        print("\nYou won 🤩")
        break
    print("\nchanse = ",chance)
    
    char=input("\nEnter a letter : ")
    if char in selectedWord:
        user_true_char.append(char)
        print("✅")
    else:
        print("❌")
        chance-=1
    
    if chance==0:
        print ("The answer is :" ,selectedWord)
        print("game over \nyou lose🙁 ")

        break