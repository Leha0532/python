import arcade

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
SCREEN_TITLE = "Пинг-понг"
BG_COLOR = (0, 25, 220)
SPEEDY = 5
SPEEDX = 5
OMG_IMG = 'plat.png'
OMG_SCALE= 0.2

BALL_IMG = 'ball_sprite.png'
BALL_SCALE = 0.2

class Ball(arcade.Sprite):
    def update(self):
        self.center_x += self.change_x
        if self.right > SCREEN_WIDTH or self.left < 0:
            self.change_x = - self.change_x
        self.center_y += self.change_y
        if self.bottom < 0 or self.top > SCREEN_HEIGHT:
            self.change_y = - self.change_y
        
class Plat(arcade.Sprite):
    def update(self):
        self.center_x += self.change_x

class GameWindow(arcade.Window):
    def __init__(self, widgth, height, title):
        super().__init__(widgth, height, title)
        self.ball = Ball(BALL_IMG, BALL_SCALE)
        self.ball.center_x = SCREEN_WIDTH//2
        self.ball.center_y = SCREEN_HEIGHT//2
        self.ball.change_x = SPEEDX
        self.ball.change_y = SPEEDY
        self.omg = Plat(OMG_IMG, OMG_SCALE)
        
        
    def on_draw(self):
        arcade.start_render()
        arcade.set_background_color(BG_COLOR)
        self.ball.draw()
        
    def update(self, delta_time: float):
        self.ball.update()
    
window = GameWindow(SCREEN_WIDTH, SCREEN_HEIGHT, "Пинг-понг")
arcade.run()