"""
Platformed Game
"""
import arcade

# Constants
SCREEN_WIDTH = 1000
SCREEN_HEIGHT = 700
SCREEN_TITLE = "Platformed"
#SPRITE_PATH = "arcade_game_1/dvd/dvd.gif"
SPRITE_PATH = "./dvd.gif"


class MyGame(arcade.Window):
    """
    Main application class.
    """

    def __init__(self):
        self.global_speed = 4
        self.speed_x = self.global_speed
        self.speed_y = self.global_speed
        self.x = 14
        self.y = 1
        self.sprite_height = 81
        self.sprite_width = 97
        # Call the parent class and set up the window
        super().__init__(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)

        arcade.set_background_color(arcade.csscolor.GREEN)
    
    def setup(self):
        """Set up the game here. Call this function to restart the game."""
        pass


    def on_update(self, delta_time):
        self.x += self.speed_x 
        self.y += self.speed_y
        if self.x > SCREEN_WIDTH - self.sprite_width//2:
            self.speed_x = -self.global_speed
        if self.y > SCREEN_HEIGHT - self.sprite_height//2:
            self.speed_y = -self.global_speed
        if self.x < 0 + self.sprite_width//2:
            self.speed_x = self.global_speed
        if self.y < 0 + self.sprite_height//2:
            self.speed_y = self.global_speed

    def on_draw(self):
        """Render the screen."""
        self.clear()
        arcade.Sprite(SPRITE_PATH, center_x=self.x, center_y=self.y, scale= 0.1).draw()
        # Code to draw the screen goes here


def main():
    """Main function"""
    window = MyGame()
    window.setup()
    arcade.run()


if __name__ == "__main__":
    main()