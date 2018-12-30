from src.player import Player
from src.world import World
from include.vector2d import Vector2D
from src.keybinds import KeybindHandler
from src import DEFAULT_KEYBINDS, GAMEDIR
from os import mkdir
from os.path import exists
from include.controls_handler import ControlsHandler


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
        self.keybinds = KeybindHandler(DEFAULT_KEYBINDS)
        self.player = Player(window, keys)
        self.world = World()
        self.controls = ControlsHandler(self.keys, self.player, self.keybinds)

    def save_game(self, game_folder_path: str):
        if not game_folder_path.endswith("/"):
            game_folder_path += "/"

        if not exists(game_folder_path):
            mkdir(game_folder_path)

        self.world.save_map(game_folder_path + "map")
        self.player.save_game(game_folder_path + "player")
        # self.keybinds.save_to_folder(game_folder_path)

        meta_data = ""

        with open(game_folder_path + "meta", "w") as meta_file:
            meta_file.write(meta_data)

    def load_game(self, game_folder_path: str):
        if not game_folder_path.endswith("/"):
            game_folder_path += "/"

        if not exists(game_folder_path):
            raise FileExistsError(f"Game save file {game_folder_path} not found")

        self.world.load_map(game_folder_path + "map")
        self.player.load_game(game_folder_path + "player")
        # self.keybinds.load_from_folder(game_folder_path)

    def on_mouse_motion(self, x, y, dx, dy):
        self.mouse_position = Vector2D(x, y)
        self.player.pos = self.mouse_position

    def on_mouse_press(self, x, y, button, mod):
        self.load_game("./saves/example")

    def mainloop(self, delta):
        self.window.clear()
        self.player.draw()
        self.player.update()
        self.controls.work()
        # print(f"keys: {self.keys};\nmouse position: {self.mouse_position}")
