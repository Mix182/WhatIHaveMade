from .Player import Player
from .Block import Block

import random

class Map:
    def __init__(self, win, player, cos, textures):
        self.win = win
        self.player = player
        self.cos = cos
        self.textures = textures

        win_size = [win.get_width(), win.get_height()]
        if win_size[0] > win_size[1]:
            self.w = win_size[1] // cos

        else:
            self.w = win_size[0] // cos

        self.x_shift = 0
        self.y_shift = 0
        self.generate_map()

    def generate_map(self):
        self.data = {}
        self.seed = int(random.random() * 10000000000000000)
        
        