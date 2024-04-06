import arcade

from arcade_game_1.bruh import SCREEN_WIDTH
from ping_pong.game import PLAT_SPEED, GameWindow

SCREEN_WEIDHT = 800
SCREEN_HEIGHT = 600
SCREEN_TITLE = "ГОНКА"

class Gamewindow(arcade.window):
    def __init__(self,widht, height, title):
        super().__init__(widht, height, title)
        
    def setup(self):
        pass
    
    def on_draw(self):
        arcade.start_render()
        pass
                 
    def on_update(self, delta_time: float):
        pass                   
    def on_key_press(self, symbol: int, modifiers: int):
        pass
    
window = GameWindow(SCREEN_WIDTH, SCREEN_HEIGHT, "Пинг-понг")
window.setup()
arcade.run()