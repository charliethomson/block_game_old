class Map:
    def __init__(self, map_file: str):
        pass

    def config(self, NAME=None, CREATION_DATE=None, CREATION_DELTA_INIT=None):

        self.name = NAME if NAME else "World"
        self.creation_date = CREATION_DATE if CREATION_DATE else "Unknown"
        self.creation_delta = CREATION_DELTA_INIT if CREATION_DELTA_INIT else 1544974037
