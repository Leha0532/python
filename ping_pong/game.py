import arcade

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
SCREEN_TITLE = "Пинг-понг"
BG_COLOR = (0, 25, 220)
SPEEDY = 5
SPEEDX = 5
PLAT_IMG = 'ping_pong/plat.png'
OMG_SCALE= 0.2

BALL_IMG = 'ping_pong/ball_sprite.png'
BALL_SCALE = 0.2
PLAT_SPEED = 5
SPEED_UP = 0.1

WIN_IMAGE = 'ping_pong/you win.webp'


class Ball(arcade.Sprite):
    def change_speed(self):
        if  self.change_x > 0:
            self.change_x += SPEED_UP
        else:
            self.change_x -= SPEED_UP
        if  self.change_y > 0:
            self.change_y += SPEED_UP
        else:
            self.change_y -= SPEED_UP

        
            
    def update(self):
        self.center_x += self.change_x
        if self.right > SCREEN_WIDTH or self.left < 0:
            self.change_x = - self.change_x
            self.change_speed()
        self.center_y += self.change_y
        if self.top > SCREEN_HEIGHT or self.bottom < 0:
            self.change_y = - self.change_y
            self.change_speed()
        
class Plat(arcade.Sprite):
    def update(self):
        self.center_x += self.change_x
        if self.left < 0:
            self.left = 0     
        if self.right > SCREEN_WIDTH:
            self.right = SCREEN_WIDTH
            
class GameWindow(arcade.Window):
    def __init__(self, widgth, height, title):
        super().__init__(widgth, height, title)
        
        self.ball = Ball(BALL_IMG, BALL_SCALE)
        self.ball.center_x = SCREEN_WIDTH//2
        self.ball.center_y = SCREEN_HEIGHT//2
        self.ball.change_x = SPEEDX
        self.ball.change_y = SPEEDY
        self.plat = Plat(PLAT_IMG, OMG_SCALE)
        self.score = 0
        self.plat.center_x = SCREEN_WIDTH//2
        self.plat.center_y = SCREEN_HEIGHT//12
        self.tries = 3
        self.game = True
        self.win = False
     
    
    def setup(self):
        self.ball.center_x = SCREEN_WIDTH/2
        self.ball.center_y = SCREEN_HEIGHT/2
        self.ball.change_x = SPEEDX
        self.ball.change_x = SPEEDX
        self.ball.center_x = SCREEN_WIDTH/2
        self.ball.center_y = SCREEN_HEIGHT/12
        
    def on_draw(self):
        arcade.start_render()
        arcade.set_background_color(BG_COLOR)
        self.ball.draw()
        self.plat.draw()
        arcade.draw_text(f"счёт: {self.score}",
                        start_x=20,
                        start_y=SCREEN_HEIGHT-20,
                        color=(255,255,255),
                        font_size=20)
        if (self.win):
            arcade.Sprite(WIN_IMAGE, 1, center_x=SCREEN_WIDTH/2, center_y=SCREEN_HEIGHT/2).draw()
                 
    def on_update(self, delta_time: float):
        if (not self.game):
            return
        self.ball.update()
        self.plat.update()
        if arcade.check_for_collision(self.ball, self.plat):
            self.ball.change_y = - self.ball.change_y
            self.ball.bottom = self.plat.top
            self.score += 40
        if self.ball.bottom < 0 :
            self.tries -= 1
            self.setup()
            if self.tries ==0:
                self.game = False
        if self.score > 30 :                   
            self.game = False
            self.win = True
    def on_key_press(self, symbol: int, modifiers: int):
        if symbol == arcade.key.RIGHT:
            self.plat.change_x = PLAT_SPEED
        if symbol == arcade.key.LEFT:
            self.plat.change_x = - PLAT_SPEED
    
window = GameWindow(SCREEN_WIDTH, SCREEN_HEIGHT, "Пинг-понг")
arcade.run()