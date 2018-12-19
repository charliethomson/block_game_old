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
        self.sprite = Sprite(PLAYER_SPRITE_IMAGE, self.pos.x, self.pos.y)

    def _terminal_velocity(self):
        if self.vel.y >= 15:
            self.vel.y = 15
            return False
        if self.vel.y <= -15:
            self.vel.y = -15
            return False
        return True

    def update(self):
        increase_speed = self._terminal_velocity()
        if increase_speed:
            self.acc -= GRAVITY
            self.vel += self.acc
        else:
            self.acc.reset()
        # self.pos += self.vel
        self.sprite.x, self.sprite.y = self.pos.x, self.pos.y
        print(self.pos, self.vel, self.acc)

    def move(self, amount: Vector2D):
        assert isinstance(amount, Vector2D), "amount must be Vector2D"
        self.pos += amount

    def draw(self):
        self.sprite.draw()
