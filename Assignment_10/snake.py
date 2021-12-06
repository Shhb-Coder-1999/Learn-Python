import random
import arcade
from arcade.key import RIGHT
from arcade.window_commands import start_render
from pyglet.libs.x11.xlib import Screen

SCREEN_WIDTH = 1000
SCREEN_HEIGHT = 1000


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

    def eat (self):
       pass  

    def draw (self):
       arcade.draw_rectangle_filled(self.center_x , self.center_y , self.width , self.height , self.color)  



class Apple(arcade.Sprite):
     def __init__(self):
        super().__init__()
        self.width = 10
        self.height = 10
        self.color = arcade.color.RED
        self.change_x = None
        self.change_y = None
        self.score = 0
        self.center_x = SCREEN_WIDTH //2
        self.center_y = SCREEN_HEIGHT //2

     def draw (self):
           arcade.draw_circle_filled(self.center_x +40, self.center_y+40 ,radius=10 , color=self.color)     

class Game(arcade.Window):
     def __init__(self):
       super().__init__(width=SCREEN_WIDTH , height=SCREEN_HEIGHT  , title="Snake Game")
       arcade.set_background_color(arcade.color.SAND)
       self.snake = Snake()
       self.apple = Apple()

     def on_draw(self):
        arcade,start_render()
        arcade.draw_text('Score : '+str(self.snake.score),start_x=20 , start_y=40 , font_size=30) 
        self.snake.draw()
        self.apple.draw()

     def on_key_release(self, symbol: int, modifiers: int):
         if  symbol == arcade.key.LEFT:
            print(symbol)
            self.snake.center_x -= 20
         elif symbol == arcade.key.RIGHT:
            self.snake.center_x += 20
         elif symbol == arcade.key.UP:
            self.snake.center_y += 20
         elif  symbol == arcade.key.DOWN: 
            self.snake.center_y -= 20


my_game = Game()
arcade.run()
