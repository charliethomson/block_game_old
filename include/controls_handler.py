from pyglet.window.key import KeyStateHandler
from src.player import Player
from src.keybinds import KeybindHandler
from include.vector2d import Vector2D


class ControlsHandler:
    def __init__(self, keys: KeyStateHandler, player: Player, keybinds: KeybindHandler):

        self.keys = keys
        self.player = player
        self.keybinds = keybinds
        self.functions = {
            self.keybinds["MOVE_RIGHT"]: (self.player.move, [Vector2D(6, 0)]),
            self.keybinds["MOVE_LEFT"]: (self.player.move, [Vector2D(-6, 0)]),
            self.keybinds["JUMP"]: (self.player.jump, None),
            self.keybinds["CROUCH"]: (self.player.crouch, None),
            self.keybinds["SPRINT"]: (self.player.sprint, None),
            self.keybinds["INVENTORY"]: (self.player.inventory, None),
        }

    def _execute_function(self, key):
        func, args = self.functions[key]
        args = args if args else []
        func(*args)

    def work(self):
        for key in list(self.functions.keys()):
            if self.keys[key]:
                self._execute_function(key)
