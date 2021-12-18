import re
import string

user_sentence = input ("Please Enter Your Sentence :")

# using regex() + string.punctuation
result = re.sub('['+string.punctuation+']', '', user_sentence).split()

print(result)