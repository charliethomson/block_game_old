from include.vector2d import Vector2D
from pyglet.image import load as load_glImage


def _setattribs(image):
    image.anchor_x, image.anchor_y = image.width // 2, 0


GRAVITY = Vector2D(0, 0.012)


PLAYER_SPRITE_FILE = "./resources/sprites/player.png"

PLAYER_SPRITE_IMAGE = load_glImage(PLAYER_SPRITE_FILE)
_setattribs(PLAYER_SPRITE_IMAGE)
