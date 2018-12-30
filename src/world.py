import time
from include.parser import parse
from src import BLOCKS


class MapLoadError(Exception):
    pass


class World:
    def __init__(self):
        self.blocks = [[]]
        self.map_name = ""
        self.creation_time = time.strftime("%a %b %d, %H:%M:%S")
        self.creation_delta = time.time()

    def _get_ids_from_blocks(self, blocks=None):
        out = []
        for array in self.blocks:
            subarray = []
            for block in array:
                subarray.append(block.id)
            out.append(subarray)
        return out

    def _get_blocks_from_ids(self, ids):
        out = []
        for array in ids:
            subarray = []
            for id_ in array:
                subarray.append(BLOCKS[id_])
            print(subarray)
            out.append(subarray)
        return out

    def load_map(self, map_file: str):
        map_data = parse(map_file)
        if map_data["MAP"] == None:
            raise MapLoadError("Error loading map, map data missing")

        self.blocks = self._get_blocks_from_ids(map_data["MAP"])
        self.map_name = map_data["MAP_NAME"]
        self.creation_delta = map_data["CREATION_DELTA_INIT"]
        self.creation_time = map_data["CREATION_TIME"]

    def save_map(self, map_file: str):
        map_data = f":MAP_NAME={self.map_name};\
        \n:CREATION_TIME={self.creation_time};\
        \n:CREATION_DELTA_INIT={self.creation_delta};\
        \n:MAP={self._get_ids_from_blocks(self.blocks)};"

        with open(map_file, "w") as file_:
            file_.write(map_data)

    def draw_map(self):
        for row in self.blocks:
            for block in row:
                block.draw()

    def generate_map(self):
        pass
