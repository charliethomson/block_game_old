from os.path import exists
from src import *


class KeybindHandler:
    def __init__(self, binds):
        self.binds = binds

    def __getitem__(self, item):
        return self.binds[item]

    def save_to_file(self, file_path):
        if not exists(file_path):
            raise FileNotFoundError(f"save file {file_path} not found")

        bindings_data = []
        for key in list(self.binds.keys()):
            bindings_data.append(f":{key.upper()}={self.binds[key]};")

        with open(file_path, "w") as file_:
            file_.write("\n".join(bindings_data))

    def load_from_folder(self, file_path):

        if not exists(file_path):
            raise FileNotFoundError(f"save folder {file_path} not found (keybinds)")

