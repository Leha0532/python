import arcade



SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
SCREEN_TITLE = "Шаблон"

DIR = "star_wars/images/"
BG_IMG = DIR + "bg.jpg"

LASER_IMG = DIR + "laser.webp"
LASER_SIZE = 0.3
LASER_SPEED = 5
LASER_SOUND = "star_wars/sounds/laser.mp3"

BG = DIR + "bg.png"

HERO_IMG = DIR + "hero.png"

HERO_SIZE = 0.2

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

class GameWindow(arcade.Window):
    def __init__(self,widht, height, title):
        super().__init__(widht, height, title)
        self.bg = arcade.load_texture(BG_IMG)
        self.spaceship = Spaceship(HERO_IMG, HERO_SIZE)
        self.lasers = arcade.SpriteList()
    
    def setup(self):
        self.spaceship.center_x = SCREEN_WIDTH/2
        self.spaceship.center_y = SCREEN_HEIGHT/4
        
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
            
    # обновление окна
    def on_update(self, delta_time):
        self.spaceship.update()
        self.lasers.update()
        
    def on_mouse_press(self, x: int, y: int, button: int, modifiers: int):
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