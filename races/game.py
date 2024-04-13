import arcade

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
SCREEN_TITLE = "ГОНКА"

BG_IMG = "races/g.png"

HERO_IMG = "races/car.png"
HERO_SIZE = 0.35
HERO_SPEED = 5
HERO_ANGLE = 90

class Hero(arcade.Sprite):
    def update(self):
        self.center_x += self.change_x

class GameWindow(arcade.Window):
    def __init__(self,widht, height, title):
        super().__init__(widht, height, title)
        self.bg = arcade.load_texture(BG_IMG)
        self.hero = Hero(HERO_IMG, HERO_SIZE)
        
    def setup(self):
        self.hero.center_x = SCREEN_WIDTH/2 + 70
        self.hero.center_y = SCREEN_HEIGHT/12
        self.hero.angle = 90
        self.hero.angle = HERO_ANGLE
    
    def on_draw(self):
        arcade.start_render()
        arcade.draw_texture_rectangle(center_x=SCREEN_WIDTH/2,
                                      center_y=SCREEN_HEIGHT/2,
                                      width=SCREEN_WIDTH,
                                      height=SCREEN_HEIGHT,
                                      texture=self.bg)
        self.hero.draw()
        
    def on_update(self, delta_time: float):
        self.hero.update()
        
    def on_key_press(self, symbol: int, modifiers: int):
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
    
window = GameWindow(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE, "Пинг-понг")
window.setup()
arcade.run()