from include.item import Item


class Block:
    def __init__(
        self,
        id_: int,
        name: str,
        sprite_path: str,
        break_rate: int = None,
        item: Item = None,
        gravity: bool = False,
    ):
        self.id_ = id_
        self.name = name
        self.break_rate = break_rate
        self.drops_item = item
        self.sprite_path = sprite_path
        self.gravity = gravity
