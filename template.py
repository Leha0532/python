import arcade


SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
SCREEN_TITLE = "Шаблон"


class GameWindow(arcade.Window):
    # конструктор, вызывается при создании объекта
    def __init__(self, width, height, title):
        super().__init__(width, height, title)
    
    # начальные координаты
    def setup(self):
        pass
    
    # отрисовка
    def on_draw(self):
        arcade.start_render()
    
    # обновление окна
    def on_update(self, delta_time):
        pass
    
    # нажатие на клавиши
    def on_key_press(self, symbol: int, modifiers: int):
        pass
    
    # отжатие на клавиши
    def on_key_release(self, symbol: int, modifiers: int):
        pass

window = GameWindow(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)
window.setup()
arcade.run()