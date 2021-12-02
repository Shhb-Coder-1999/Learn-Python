# !pip install pyTelegramBotAPI
# !pip install Khayyam
# !pip install gTTS
# !pip install qrcode[pil]
# https://github.com/eternnoir/pyTelegramBotAPI 

import telebot
import random
from khayyam import JalaliDatetime
from gtts import gTTS
import qrcode

bot = telebot.TeleBot("2137470201:AAFqMjvwzbRCo_WRfn23fchPD2xQdS-n3j0")

@bot.message_handler(commands=['start'])
def hello(message):
  bot.reply_to(message, "Welcome to my bot " +  message.from_user.first_name +  " ! click on /help to get more info")

btn=None
random_number = 0

@bot.message_handler(commands=['game'])
def game(message):
  global random_number
  global btn
  random_number = random.randint(0,50)
  btn = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True)
  content = telebot.types.KeyboardButton('New Game')
  btn.add(content)
  bot.reply_to(message,"Guess a number Please between 0 , 50 ") 
  bot.register_next_step_handler(message , Get_Number)

def Get_Number(message):
    global btn
    if message.text == 'New Game':
      msg = bot.send_message(message.chat.id, 'new game started')
      game(msg)
    elif int(message.text) > random_number:
      bot.reply_to(message, "Greater than Goal Number , plz try again !" , reply_markup=btn )
      bot.register_next_step_handler(message , Get_Number)
    elif int(message.text) < random_number :
      bot.reply_to(message, "Smaller than Goal Number , plz try again !" , reply_markup=btn )
      bot.register_next_step_handler(message , Get_Number)
    elif int(message.text) == random_number:
      bot.send_message(message.chat.id, 'nice !! you find it:)', reply_markup=btn )
      

    

@bot.message_handler(commands=['age'])
def age(message):
  bot.reply_to(message,"Please enter your birth date (example 1378/9/23)") 
  bot.register_next_step_handler(message , Cal_Age)

def Cal_Age(message):
    date = message.text.split('/')
    dif = JalaliDatetime.now()-JalaliDatetime(date[0],date[1],date[2])
    bot.reply_to(message,round(int(dif.days)/365))

@bot.message_handler(commands=['TextToVoice'])
def TextToVoice(message):
  bot.reply_to(message,"please enter your text :") 
  bot.register_next_step_handler(message , Text_To_Voice)

def Text_To_Voice(message):
    mytext = message.text
    language = 'en'
    myobj = gTTS(text=mytext , lang=language , slow=False)
    myobj.save("voice.ogg")
    myobj = open('voice.ogg', 'rb')
    bot.send_voice(message.chat.id, myobj)

@bot.message_handler(commands=['FindGreatestNumber'])
def FindGreatestNumber(message):
  bot.reply_to(message,"Enter elements of a list separated by space :") 
  bot.register_next_step_handler(message , Find_Greatest_Number)

def Find_Greatest_Number(message):
    user_list = message.text.split() 
    bot.reply_to(message, max(user_list)) 

@bot.message_handler(commands=['FindGreatestNumberIndex'])
def FindGreatestNumberIndex(message):
  bot.reply_to(message,"Enter elements of a list separated by space :") 
  bot.register_next_step_handler(message , Find_Greatest_Number_Index)

def Find_Greatest_Number_Index(message):
    user_list = message.text.split() 
    bot.reply_to(message, user_list.index(max(user_list))) 

@bot.message_handler(commands=['Qrcode'])
def Qr(message):
  bot.reply_to(message,"Enter your text :") 
  bot.register_next_step_handler(message , qr)

def qr(message):
    img = qrcode.make(message.text) 
    img.save('qrcode.png')
    photo = open('qrcode.png', 'rb')
    bot.send_photo(message.chat.id, photo)
          

@bot.message_handler(commands=['help'])
def help(message):
   bot.reply_to(message,
                 """
                 /start - welcome to my bot
/game  = guess the number 
/age  = calculate your age 
/TextToVoice  = convert text to voice 
/FindGreatestNumber = find greatest number 
/FindGreatestNumberIndex = find index of greatest number 
/Qrcode = make Qrcode  
/help = menu""" )


@bot.message_handler(func=lambda m: True)
def echo_all(message):
    bot.reply_to(message, "Cant undersyand what did you say !! please click on /help to get more info") 


bot.infinity_polling()  