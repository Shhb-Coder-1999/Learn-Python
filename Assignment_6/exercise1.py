WORDS = []
import sys
import re

def Load_Data():
    try: 
        with open ('/media/shb/3C50BD1450BCD63C/programming/Github/Learn_Python/Assignment_6/words_bank.txt','r') as f:
         big_text = f.read()
         lines = big_text.split('\n')

         for i in range(0,len(lines),2):
            WORDS.append( {'english':lines[i] , 'persion':lines[i+1]})
        f.close()    

    except OSError:
      print ("Could not open read file ")
      sys.exit()


def translate_en2fa(input_text):
    user_words = re.findall(r"[\w']+|[.,!?;]", input_text)

    output_text = ""

    for user_word in user_words :
        for WORD in WORDS :
            if user_word == WORD['english']:
                output_text  += WORD['persion'] + " "
                break
        else :
         output_text  += user_word + " "  

    return output_text   

def translate_fa2en(input_text):
    user_words = re.findall(r"[\w']+|[.,!?;]", input_text)

    output_text = ""

    for user_word in user_words :
        for WORD in WORDS :
            if user_word ==  WORD['persion'] :
                output_text  += WORD['english'] + " "
                break
        else :
         output_text  += user_word + " "  

    return output_text       



Load_Data()


menu_options = {
    1: 'Add new word',
    2: 'Translate_en2fa',
    3: 'Translate_fa2en',
    4: 'Exit',
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
           en_word = input ('please write your english word :')
           fa_word = input ('please write your persian word :') 
           WORDS.append( {'english':en_word  , 'persion':fa_word}) 
           with open('/media/shb/3C50BD1450BCD63C/programming/Github/Learn_Python/Assignment_6/words_bank.txt', "a") as myfile:
             myfile.write("\n")
             myfile.write(en_word)
             myfile.write("\n")
             myfile.write(fa_word)
             myfile.close() 

        elif option == 2:
            print(translate_en2fa(input ('please write your text :')))

        elif option == 3:
            print(translate_fa2en(input ('please write your text :')))    

        elif option == 4:
            print('Thanks message before exiting')
            exit()
        else:
            print('Invalid option. Please enter a number between 1 and 4.')