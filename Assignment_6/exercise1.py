WORDS = []

def Load_Data():
    with open ('/media/shb/3C50BD1450BCD63C/programming/Github/Learn_Python/Assignment_6/words_bank.txt','r') as f:
        big_text = f.read()
        lines = big_text.split('\n')

        for i in range(0,len(lines),2):
            WORDS.append( {'english':lines[i] , 'persion':lines[i+1]})

Load_Data()
user_text = input ('please write your text :')
user_words = user_text.split(' ')

print(user_words)

output_text = ""

for user_word in user_words :
    for WORD in WORDS :
        if user_word == WORD['english']:
            output_text  += WORD['persion'] + " "
    else :
      output_text  += user_word + " "  

print(output_text)