from include.vector2d import Vector2D
from pyglet.sprite import Sprite
from pyglet.image import load as load_image
from src import *


class Player:
    def __init__(self, window, keys):
        self.window = window
        self.keys = keys
        self.pos = Vector2D(self.window.width // 2, self.window.height // 2)
        self.globalpos = Vector2D()
        self.vel = Vector2D()
        self.acc = Vector2D()
        self.health = 100
        self.sprite = Sprite(PLAYER_SPRITE_IMAGE, self.pos.x, self.pos.y)

    def __repr__(self):
        return f"""
Player data:
    pos: {self.pos}
    global pos: {self.globalpos}
    vel: {self.vel}
    acc: {self.acc}
    health: {self.health}"""

    def _terminal_velocity(self):
        if self.vel.y >= 15:
            self.vel.y = 15
            return False
        if self.vel.y <= -15:
            self.vel.y = -15
            return False
        return True

    def update(self):
        if self._terminal_velocity():
            self.acc -= GRAVITY
            self.vel += self.acc
        else:
            self.acc.reset()
        # self.pos += self.vel
        self.sprite.x, self.sprite.y = self.pos.x, self.pos.y
        print(self)

    def move(self, amount: Vector2D):
        assert isinstance(amount, Vector2D), "amount must be Vector2D"
        self.pos += amount

    def draw(self):
        self.sprite.draw()

    def save_game(self, save_file):
        player_data = f""":POS={self.pos};\n:GLOBAL={self.globalpos};\n:VEL={self.vel};\n:ACC={self.acc};\n:HEALTH={self.health};"""

        with open(save_file, "w") as file_:
            file_.write(player_data)

    def load_game(self, save_file):
        with open(save_dile, "r") as file_:
            player_data = file_.read()

        

