from src.player import Player
from include.vector2d import Vector2D


class Game:
    def __init__(self, window, keys):
        """
        Initialise the game
        params:
        window:
            <pyglet.window.Window>
            The window in which the game is being run
        keys:
            <pyglet.window.key.KeyStateHandler>
            Holds a dictionary of currently pressed and released keys
        """
        self.window = window
        self.keys = keys
        self.mouse_position = Vector2D()
        self.keybinds = {}
        self.player = Player(window, keys)

    def save_game(self, game_folder_path: str):
        pass
    
    def load_game(self, game_folder_path: str):
        pass

    def on_mouse_motion(self, x, y, dx, dy):
        self.mouse_position = Vector2D(x, y)
        self.player.pos = self.mouse_position

    def on_mouse_press(self, x, y, button, mod):
        pass

    def mainloop(self, delta):
        self.window.clear()
        self.player.draw()
        self.player.update()
        print(f"keys: {self.keys};\nmouse position: {self.mouse_position}")
