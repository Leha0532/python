"""
Platformed Game
"""
import arcade

# Constants
SCREEN_WIDTH = 1000
SCREEN_HEIGHT = 700
SCREEN_TITLE = "Platformed"


class MyGame(arcade.Window):
    """
    Main application class.
    """

    def __init__(self):

        # Call the parent class and set up the window
        super().__init__(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)
        arcade.set_background_color(arcade.csscolor.ALICE_BLUE)
    

    def setup(self):
        """Set up the game here. Call this function to restart the game."""
        self.x = 5
        self.y = 5
        pass

    def on_draw(self):
        """Render the screen."""
        self.clear()
        # Code to draw the screen goes here
        arcade.Sprite(":resources:images/tiles/boxCrate_double.png", 1, center_x=100, center_y=100).draw()
        arcade.draw_circle_filled(self.x, self.y, 50, arcade.csscolor.BLACK)
        
    
    def on_key_press(self, symbol: int, modifiers: int):
        if symbol == arcade.key.UP:
            self.y += 10



def main():
    """Main function"""
    window = MyGame()
    window.setup()
    arcade.run()


if __name__ == "__main__":
    main()