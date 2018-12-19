import time


class World:
    def __init__(self):
        self.blocks = [[]]
        self.map_name = ""
        self.creation_time = time.strftime("%a %b %d, %H:%M:%S")
        self.creation_delta = time.time()

    def load_map(self, map_file: str):
        pass

    def save_map(self, map_file: str):
        with open(map_file, "w") as file_:
            file_.write()
