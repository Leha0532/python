import arcade



SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
SCREEN_TITLE = "Шаблон"

BG_IMG = "star_wars/images/bg.jpg"

dir = "star_wars/images/"

BG = dir + "bg.png"

HERO_IMG = dir + "hero.png"

HERO_SIZE = 0.2

class laser(arcade.Sprite):
    def __init__(Self):
        super().__init__()

class Spaceship(arcade.Sprite):
    def update (self):
        self.center_x += self.change_x

class GameWindow(arcade.Window):
    def __init__(self,widht, height, title):
        super().__init__(widht, height, title)
        self.bg = arcade.load_texture(BG_IMG)
        self.spaceship = Spaceship(HERO_IMG, HERO_SIZE)
    
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
    
    # обновление окна
    def on_update(self, delta_time):
        self.spaceship.update()


    def on_mouse_motion(self, x: int, y: int, dx: int, dy: int):
        self.spaceship.center_x = x
        self.set_mouse_visible(False)

window = GameWindow(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)
window.setup()
arcade.run()