import random
import arcade
import time
import math

from arcade.key import RIGHT

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 800


class Airplane:
    # ersbari dade shavad
    pass

class SpaceShip(arcade.Sprite):
    def __init__(self):
        super().__init__(':resources:images/space_shooter/playerShip1_blue.png')
        self.HP = "photo_2021-12-17_17-08-38.jpg"
        self.HP1 = [arcade.Sprite(self.HP, 0.08 , center_x=SCREEN_WIDTH-10 , center_y=10) , arcade.Sprite(self.HP, 0.08 , center_x=SCREEN_WIDTH-40 , center_y=10) ,arcade.Sprite(self.HP, 0.08 ,center_x=SCREEN_WIDTH-70 , center_y=10)]
        self.width = 48
        self.height = 48
        self.score = 0
        self.center_x = SCREEN_WIDTH //2
        self.center_y =  32
        self.angle = 0
        self.change_angle = 1
        self.speed = 4
        self.bullet_list = []

    def move(self):
        self.center_y -= self.speed  

    def fire(self):
        self.bullet_list.append(Bullet(self))

    def rotate(self):
        self.angle += self.speed * self.change_angle   

    def draw(self):
        for h in self.HP1:
            h.draw()  

        return super().draw()       




class Enemy(arcade.Sprite):
     def __init__(self):
        super().__init__(":resources:images/space_shooter/playerShip1_orange.png")
        self.width = 48
        self.height = 48
        self.center_x = random.randint(self.width ,SCREEN_WIDTH - self.width)
        self.center_y = SCREEN_HEIGHT + self.height//2  
        # self.angle = 0
        # self.change_angle = 1
        self.speed = 4

     def move(self):
            self.center_y -= self.speed  

class Bullet(arcade.Sprite):
    def __init__(self , host):
        super().__init__(":resources:images/space_shooter/laserRed01.png")
        self.width = 10
        self.height = 4
        self.center_x = host.center_x 
        self.center_y = host.center_y  
        self.angle = host.angle
        self.speed = 6
        

    def move(self):
        a = math.radians(self.angle)
        self.center_x -= self.speed * math.sin(a)
        self.center_y += self.speed * math.cos(a)


class Game(arcade.Window):
    def __init__(self):
        super().__init__(SCREEN_WIDTH,SCREEN_HEIGHT,"SHHB GAME")
        arcade.set_background_color(arcade.color.SAND)
        self.background_image = arcade.load_texture(":resources:images/backgrounds/abstract_1.jpg")
        self.me = SpaceShip()
        self.enemy_list = []
        self.score = 0
        self.start_time = time.time()

    def on_draw(self):
        arcade.start_render()
        arcade.draw_lrwh_rectangle_textured(0,0,SCREEN_WIDTH ,SCREEN_HEIGHT,self.background_image )
        self.me.draw()
 
        for enemy in self.enemy_list:
            enemy.draw()

        for b in self.me.bullet_list:
            b.draw()

       
                

        arcade.draw_text('Score : '+str(self.score),start_x=20 , start_y=40 , font_size=20)                   

    def on_update(self, delta_time: float):
        self.end_time = time.time()

        if self.end_time - self.start_time > 5:
            self.enemy_list.append(Enemy())
            self.start_time = time.time()

        self.me.rotate()

        for enemy in self.enemy_list:
            enemy.move()

        for b in self.me.bullet_list:
            b.move()  


        for enemy in self.enemy_list:
          for b in self.me.bullet_list:
              if arcade.check_for_collision(enemy,b):
                  self.enemy_list.remove(enemy)
                  self.score += 1
           
            

         

    def on_key_press(self, symbol: int, modifiers: int):
        if symbol == arcade.key.SPACE:
            self.me.fire() 
        elif symbol == arcade.key.LEFT:
            self.me.change_angle = 1
        elif symbol == arcade.key.RIGHT:
            self.me.change_angle = -1              

game = Game()
arcade.run()        