from include.vector2d import Vector2D
from pyglet.image import load as load_glImage
from include.parser import parse
from include.block import Block


def _setattribs(image):
    image.anchor_x, image.anchor_y = image.width // 2, 0


def _get_blocks(ids):
    blocks = {}
    sprites = parse("./resources/id_to_spritepath")
    print(sprites)
    for key in list(ids.keys()):
        value = ids[key]

    return blocks


GRAVITY = Vector2D(0, 0.012)

GAMEDIR = "/run/media/charlie/CTH1/development/python/working_on/block_game/"

PLAYER_DEFAULT_SPRITE_FILE = "./resources/sprites/player.png"
PLAYER_DEFAULT_SPRITE_IMAGE = load_glImage(PLAYER_DEFAULT_SPRITE_FILE)
_setattribs(PLAYER_DEFAULT_SPRITE_IMAGE)


DEFAULT_KEYBINDS = parse("./resources/default_keybinds", keybinds=True)

BLOCK_IDS = parse("./resources/block_ids")
print(BLOCK_IDS)
BLOCKS = _get_blocks(BLOCK_IDS)
