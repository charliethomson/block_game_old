from os.path import exists
from src import *

class KeybindHandler:
    def __init__(self, binds):
        self.binds = binds

    def save_to_folder(self, file_path):
        if not exists(file_path):
            raise FileNotFoundError(f"save folder {file_path} not found (keybinds)")
        
        bindings_data = []
        for key in list(self.binds.keys()):
            bindings_data.append(f":{key.upper()}={self.binds[key]};")
        
        with open(file_path + "keybinds", "w") as file_:
            file_.write("\n".join(bindings_data))