# !pip install pyTelegramBotAPI
# !pip install Khayyam
# https://github.com/eternnoir/pyTelegramBotAPI 
# https://www.heroku.com/

import telebot
import random
from khayyam import JalaliDatetime


bot = telebot.TeleBot("2137470201:AAFqMjvwzbRCo_WRfn23fchPD2xQdS-n3j0")

@bot.message_handler(commands=['start'])
def hello(message):
  bot.reply_to(message, "Welcome to my bot " +  message.from_user.first_name +  " !")


random_number = random.randint(0,50)
@bot.message_handler(commands=['game'])
def game(message):
  bot.reply_to(message,"Guess a number Please") 
  bot.register_next_step_handler(message , Get_Number)

def Get_Number(message):
    if int(message.text) > random_number:
      bot.reply_to(message, "Greater than Goal Number , plz try again !")
      bot.register_next_step_handler(message , Get_Number)
    elif int(message.text) < random_number :
      bot.reply_to(message, "Smaller than Goal Number , plz try again !")
      bot.register_next_step_handler(message , Get_Number)
    elif int(message.text) == random_number:
      bot.reply_to(message, "Nice !!")
    

@bot.message_handler(commands=['age'])
def game(message):
  bot.reply_to(message,"Please enter your birth date (example 1378/9/23)") 
  bot.register_next_step_handler(message , Cal_Age)

def Cal_Age(message):
    date = message.text.split('/')
    dif = JalaliDatetime.now()-JalaliDatetime(date[0],date[1],date[2])
    bot.reply_to(message,round(int(dif.days)/365))
  

@bot.message_handler(commands=['help'])
def help(message):
  bot.reply_to(message,"How Can I Help You ?? What Do You Need Right Now? ") 

fals =['1','2','3']
@bot.message_handler(commands=['fal']) 
def fal(message):
  x = random.choice(fals)
  bot.reply_to(message,x)

@bot.message_handler(func=lambda m: True)
def echo_all(message):
  if message.text == "Hello":
    bot.reply_to(message, "Hi")
  elif message.text == "How Are you?":
    bot.reply_to(message, "tnx and you ?")
  elif message.text == "bye":
    bot.reply_to(message, "ok bye !") 
  elif   message.text == "sent photo":
    my_photo = open ("default-logo_mail-1431892093.jpg‏","rb")
    bot.send_photo(message.chat.id , my_photo)

  else :
    bot.reply_to(message, "Cant undersyand what did you say !!") 


bot.infinity_polling()  