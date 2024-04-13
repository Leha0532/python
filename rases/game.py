import arcade

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
SCREEN_TITLE = "ГОНКА"

class GameWindow(arcade.Window):
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