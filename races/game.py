import arcade
import random

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
SCREEN_TITLE = "ГОНКА"

BG_IMG = "races/g.png"
LOST_BG = "races/lost.png"
HERO_IMG = "races/car.png"
HERO_SIZE = 0.25
HERO_SPEED = 10
HERO_ANGLE = 90
CUCUMBER_IMG = 'races/cu.png'
CUCUMBER_SIZE = 0.05
CU_SPEED = 500

class Cu(arcade.Sprite):
    def update(self):
        self.center_y -= self.change_y
        if self.top < 0:
            self.bottom = random.randint(SCREEN_HEIGHT,SCREEN_HEIGHT*2)
            self.center_x = random.randint(30,SCREEN_WIDTH -30)
    
class Hero(arcade.Sprite):
    def update(self):
        self.center_x += self.change_x
        m = 30
        if self.center_x  > SCREEN_WIDTH - m:
            self.center_x = SCREEN_WIDTH - m

        if self.center_x  < 0 + m:
            self.center_x = 0 + m

class GameWindow(arcade.Window):
    def __init__(self,widht, height, title):
        super().__init__(widht, height, title)
        self.bg = arcade.load_texture(BG_IMG)
        self.lost_bg = 'races\lost.png'
        
        self.hero = Hero(HERO_IMG, HERO_SIZE)
        self.cu = Cu(CUCUMBER_IMG, CUCUMBER_SIZE)
        self.game = True
        
        
    def setup(self):
        self.hero.center_x = SCREEN_WIDTH/2 + 70
        self.hero.center_y = SCREEN_HEIGHT/12 + 70
        self.cu.center_x = 500
        self.cu.center_y = 500
        self.hero.angle = 90
        self.hero.angle = HERO_ANGLE
        self.cu.change_y = CU_SPEED
    
    def on_draw(self):
        arcade.start_render()
        arcade.draw_texture_rectangle(center_x=SCREEN_WIDTH/2,
                                      center_y=SCREEN_HEIGHT/2,
                                      width=SCREEN_WIDTH,
                                      height=SCREEN_HEIGHT,
                                      texture=self.bg)
        self.hero.draw()
        self.cu.draw()
        if not self.game:
            arcade.draw_texture_rectangle(center_x=SCREEN_WIDTH/2,
                                      center_y=SCREEN_HEIGHT/2,
                                      width=SCREEN_WIDTH,
                                      height=SCREEN_HEIGHT,
                                      texture=self.lost_bg)
        
        self.hero.draw()
        self.cu.draw()
        
        
    def on_update(self, delta_time):
        if self.game:
            self.hero.update()
            self.cu.update()
            if arcade.check_for_collision(self.hero, self.cu):
                self.game = False
        
    def on_key_press(self, symbol: int, modifiers: int):
        if self.game:
            
            if symbol == arcade.key.RIGHT:
                self.hero.change_x = HERO_SPEED
                self.hero.angle = HERO_ANGLE - 20 
            if symbol == arcade.key.LEFT:
                self.hero.change_x = - HERO_SPEED
                self.hero.angle = HERO_ANGLE + 20
    
    def on_key_release(self, symbol: int, modifiers: int):
        if symbol == arcade.key.RIGHT or symbol == arcade.key.LEFT:
            self.hero.change_x = 0
            self.hero.angle = HERO_ANGLE
    
window = GameWindow(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)
window.setup()
arcade.run()