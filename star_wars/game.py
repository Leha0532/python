import arcade
import random


SCREEN_WIDTH = 1000
SCREEN_HEIGHT = 600
SCREEN_TITLE = "Шаблон"

DIR = "star_wars/images/"
BG_IMG = DIR + "bg.jpg"

LASER_IMG = DIR + "laser.webp"
LASER_SIZE = 0.3
LASER_SPEED = 5
LASER_SOUND = "star_wars/sounds/laser.mp3"



HERO_IMG = DIR + "hero.png"

ENEMY_DISTANCE = 1

ENEMY_COUNT = 1

HERO_SIZE = 0.2

ENEMY_SIZE = 0.08

ENEMY_SPEED = -2

ENEMY_IMG = DIR + "enemy.png"

WIN_BG = DIR + "pobeda.jpg"

class Laser(arcade.Sprite):
    def __init__(self):
        super().__init__(LASER_IMG, LASER_SIZE)
        self.bottom = window.spaceship.top
        self.center_x = window.spaceship.center_x
        self.change_y = LASER_SPEED
        self.sound = arcade.load_sound(LASER_SOUND)
        
    def update(self):
        self.center_y += self.change_y
        if self.bottom > SCREEN_HEIGHT:
            self.kill()

class Spaceship(arcade.Sprite):
    def update (self):
        self.center_x += self.change_x

class Enemy(arcade.Sprite):
    def __init__(self):
        super().__init__(ENEMY_IMG, ENEMY_SIZE)
        self.center_x = random.randint(70,SCREEN_WIDTH-70)
        self.change_y = ENEMY_SPEED
             
    def update(self):
        self.center_y += self.change_y - 0.5
        if self.top < 0:
            self.kill()        

class GameWindow(arcade.Window):
    def __init__(self,widht, height, title):
        super().__init__(widht, height, title)
        self.bg = arcade.load_texture(BG_IMG)
        self.win_bg = arcade.load_texture(WIN_BG)
        
        self.spaceship = Spaceship(HERO_IMG, HERO_SIZE)
        self.lasers = arcade.SpriteList()
        self.enemies = arcade.SpriteList()
        self.win = False
    
    def setup(self):
        self.spaceship.center_x = SCREEN_WIDTH/2
        self.spaceship.center_y = SCREEN_HEIGHT/4

        for i in range(ENEMY_COUNT):
            enemy = Enemy()
            enemy.center_y = SCREEN_HEIGHT + i* ENEMY_DISTANCE
            self.enemies.append(enemy)
            
    # отрисовка
    def on_draw(self):
        arcade.start_render()
        arcade.draw_texture_rectangle(center_x=SCREEN_WIDTH/2,
                                    center_y=SCREEN_HEIGHT/2,
                                    width=SCREEN_WIDTH,
                                    height=SCREEN_HEIGHT,
                                    texture=self.bg)
        
        self.spaceship.draw()
        self.lasers.draw()
        self.enemies.draw()
        if self.win:
             arcade.draw_texture_rectangle(center_x=SCREEN_WIDTH/2,
                                    center_y=SCREEN_HEIGHT/2,
                                    width=SCREEN_WIDTH,
                                    height=SCREEN_HEIGHT,
                                    texture=self.win_bg)
    # обновление окна
    def on_update(self, delta_time):
        self.spaceship.update()
        self.lasers.update()
        self.enemies.update()
        for laser in self.lasers:
            hit_list = arcade.check_for_collision_with_list(laser, self.enemies)
            if hit_list:
                laser.kill()
                for enemy in hit_list:
                    enemy.kill()
        if len(self.enemies) == 0:
            self.win = True
        
    def on_mouse_press(self, x: int, y: int, button: int, modifiers: int):
        if not self.win:
            if button == arcade.MOUSE_BUTTON_LEFT:
                laser = Laser()
                self.lasers.append(laser)
                arcade.play_sound(laser.sound, 0.2)

    def on_mouse_motion(self, x: int, y: int, dx: int, dy: int):
        self.spaceship.center_x = x
        self.set_mouse_visible(False)
        if self.spaceship.center_x > SCREEN_WIDTH:
            self.spaceship.center_x = SCREEN_WIDTH
            

        if self.spaceship.center_x < 0:
            self.spaceship.center_x = 0

window = GameWindow(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)
window.setup()
arcade.run()