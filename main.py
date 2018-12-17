from pyglet.app import run as run_app
from pyglet.clock import schedule
from pyglet.window import Window
from pyglet.window.key import KeyStateHandler
from src.game import Game

window = Window(1000, 1000)
keys = KeyStateHandler()
window.push_handlers(keys)
game = Game(window, keys)
# game.setup()


@window.event
def on_mouse_motion(x, y, dx, dy):
    game.on_mouse_motion(x, y, dx, dy)


@window.event
def on_mouse_press(x, y, button, mod):
    game.on_mouse_press(x, y, button, mod)


@window.event
def on_mouse_drag(x, y, dx, dy, button, mod):
    game.on_mouse_motion(x, y, dx, dy)
    game.on_mouse_press(x, y, button, mod)

schedule(game.mainloop)
if __name__ == "__main__":
    run_app()

