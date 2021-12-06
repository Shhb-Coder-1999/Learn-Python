import random
import arcade
import arcade.gui
from arcade.key import RIGHT
from arcade.window_commands import start_render
from pyglet.libs.x11.xlib import Screen

SCREEN_WIDTH = 1000
SCREEN_HEIGHT = 1000

class QuitButton(arcade.gui.UIFlatButton):
    def on_click(self, event: arcade.gui.UIOnClickEvent):
        arcade.exit()


class Snake(arcade.Sprite):
    def __init__(self):
        super().__init__()
        self.width = 30
        self.height = 30
        self.color = arcade.color.GREEN
        self.change_x = None
        self.change_y = None
        self.score = 0
        self.center_x = SCREEN_WIDTH //2
        self.center_y = SCREEN_HEIGHT //2

    def move (self):
       pass

    def eat (self , obj_x , obj_y , obj_type):
       if self.center_y == obj_y and self.center_x  == obj_x :
         if obj_type == 'apple':      
           self.score = self.score + 1
           return True
         elif obj_type == 'pear':
           self.score = self.score + 2
           return True 
         elif obj_type == 'hitch':
           self.score = self.score - 1  
           return True       

    def draw (self):
       arcade.draw_rectangle_filled(self.center_x , self.center_y , self.width , self.height , self.color)  



class Apple(arcade.Sprite):
     def __init__(self):
        super().__init__()
        self.image = '/media/shb/3C50BD1450BCD63C/programming/Github/Learn_Python/Assignment_10/apple.png'
        self.apple = arcade.Sprite(self.image, 0.10)
        self.apple.center_x  = random.randrange(60, SCREEN_HEIGHT , 20) 
        self.apple.center_y  = random.randrange(60, SCREEN_WIDTH , 20) 

     def draw(self):
        self.apple.draw()

class Pear(arcade.Sprite):
     def __init__(self):
        super().__init__()
        self.image = '/media/shb/3C50BD1450BCD63C/programming/Github/Learn_Python/Assignment_10/pear.png'
        self.pear = arcade.Sprite(self.image, 0.08)
        self.pear.center_x  = random.randrange(60, SCREEN_HEIGHT , 20) 
        self.pear.center_y  = random.randrange(60, SCREEN_WIDTH , 20) 

     def draw(self):
        self.pear.draw()  

class Hitch(arcade.Sprite):
     def __init__(self):
        super().__init__()
        self.image = '/media/shb/3C50BD1450BCD63C/programming/Github/Learn_Python/Assignment_10/shit.png'
        self.hitch = arcade.Sprite(self.image, 0.08)
        self.hitch.center_x  = random.randrange(60, SCREEN_HEIGHT , 20) 
        self.hitch.center_y  = random.randrange(60, SCREEN_WIDTH , 20) 

     def draw(self):
        self.hitch.draw()                
             

class Game(arcade.Window):
     def __init__(self):
       super().__init__(width=SCREEN_WIDTH , height=SCREEN_HEIGHT  , title="Snake Game")
       arcade.set_background_color(arcade.color.SAND)
       self.snake = Snake()
       self.apple = Apple()
       self.pear = Pear()
       self.hitch = Hitch()
       

     def on_draw(self):
        arcade,start_render()
        arcade.draw_text('Score : '+str(self.snake.score),start_x=20 , start_y=40 , font_size=30) 
        self.snake.draw()
        self.apple.draw()
        self.pear.draw()
        self.hitch.draw()
     
     def on_key_release(self, symbol: int, modifiers: int):
         if  symbol == arcade.key.LEFT:
            self.snake.center_x -= 20
            self.check_pos()
                
         elif symbol == arcade.key.RIGHT:
            self.snake.center_x += 20
            self.check_pos()

         elif symbol == arcade.key.UP:
            self.snake.center_y += 20
            self.check_pos()

         elif symbol == arcade.key.DOWN:
            self.snake.center_y -= 20
            self.check_pos()
             
     def check_pos(self):
            
        if self.snake.eat(self.apple.apple.center_x , self.apple.apple.center_y ,'apple') == True:  
                  self.apple.apple.center_x = random.randrange(60, SCREEN_HEIGHT - self.apple.center_x , 20) 
                  self.apple.apple.center_y = random.randrange(60, SCREEN_WIDTH - self.apple.center_y , 20)

        elif self.snake.eat(self.pear.pear.center_x , self.pear.pear.center_y ,'pear') == True:  
                  self.pear.pear.center_x = random.randrange(60, SCREEN_HEIGHT - self.pear.center_x , 20) 
                  self.pear.pear.center_y = random.randrange(60, SCREEN_WIDTH - self.pear.center_y , 20)

        elif self.snake.eat(self.hitch.hitch.center_x , self.hitch.hitch.center_y ,'hitch') == True:  
                  self.hitch.hitch.center_x = random.randrange(60, SCREEN_HEIGHT - self.hitch.center_x , 20) 
                  self.hitch.hitch.center_y = random.randrange(60, SCREEN_WIDTH - self.hitch.center_y , 20)                    



       



my_game = Game()
arcade.run()
