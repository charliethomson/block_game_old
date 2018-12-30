from include.item import Item
from include.parser import parse


class Block:
    def __init__(
        self,
        id_: int,
        name: str,
        sprite_path: str = None,
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

    @classmethod
    def from_dict(cls, block_data: dict):

        assert isinstance(
            block_data, dict
        ), f"Cannot create block object from type {type(block_data)}"

        


    @classmethod
    def from_file(cls, file_path: str):
        reqds = [
            "BLOCK_ID",
            "BLOCK_NAME",
            "BREAK",
            "DROPS_ITEM",
            "SPRITE_PATH",
            "GRAVITY",
        ]

        defs = [-1, "BLOCK_ID_MISSING", 0, None, None, False]
        Block.from_dict(parse(file_path, reqds=reqds, defaults=defs))
