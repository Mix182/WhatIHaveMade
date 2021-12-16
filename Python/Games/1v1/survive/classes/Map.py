from classes.Player import Player
import pygame

from .Rails import Railway
from .Spawner import Spawner
from .Player import Player

from .copy import copy

class Map:
    def __init__(self, win, maps, textures, players=["Name1", "Name2", "Name3", "Name4"], map_type="default", rect=[], blocks={".": "air", "#": "block", "C": "S - shooter", "-": "S - Railways", "S": "S - spawner", "1": "S - player1", "2": "S - player2", "3": "S - player3", "4": "S - player4", "P": "S - Player"}, theme="default", correction=True, scene=None):
        self.win = win
        self.players = players
        self.pc = len(players)
        self.maps = maps
        self.textures = textures[theme]

        self.mt = map_type
        self.rect = rect
        self.blocks = blocks

        self.scene = scene

        if rect == []:
            self.ws = {"w": win.get_width(), "h": win.get_height()}
            self.offset = [0, 0]

        else:
            self.ws = {"w": rect[2], "h": rect[3]}
            self.offset = [rect[0], rect[1]]

        self.corr = correction

        self.generate_map()
    def generate_map(self):
        map = self.maps[self.mt]
        self.data = copy(map["map"])

        if self.corr:
            self.ssw = self.ws["w"] // len(self.data[0])
            self.ssh = self.ws["h"] // len(self.data)
            if self.ssw < self.ssh:
                self.offset = [0, (self.ws["h"] - (self.ssw * len(self.data))) // 2]
                self.ws = {"w": self.win.get_width(), "h": self.ssw * len(self.data)}

            elif self.ssw > self.ssh:
                self.offset = [(self.ws["w"] - (self.ssh * len(self.data[0]))) // 2, 0]
                self.ws = {"w": self.ssh * len(self.data[0]), "h": self.win.get_height()}

        self.entities = []

        self.ssw = self.ws["w"] // len(self.data[0])
        self.ssh = self.ws["h"] // len(self.data)

        for y in range(len(self.data)):
            for x in range(len(self.data[y])):
                block = self.data[y][x]
                if not block in self.blocks:
                    block = "."

                if self.blocks[block].startswith("S - "):
                    image = self.textures["Blocks"][self.blocks["."]]["0"]

                    if self.blocks[block] == "S - Railways" or self.blocks[block] == "S - shooter":
                        blcks = [list(self.blocks.keys())[list(self.blocks.values()).index("S - Railways")]]
                        blcks.append(list(self.blocks.keys())[list(self.blocks.values()).index("S - shooter")])

                        inputs = []
                        if map["map"][y-1][x] in blcks:
                            inputs.append("up")

                        if map["map"][y+1][x] in blcks:
                            inputs.append("down")

                        if map["map"][y][x-1] in blcks:
                            inputs.append("left")

                        if map["map"][y][x+1] in blcks:
                            inputs.append("right")

                        self.entities.append(Railway(self.win, (x * self.ssw) + self.offset[0], (y * self.ssh) + self.offset[1], x, y, self.ssw, self.ssh, self.textures["Blocks"]["Railways"], inputs))

                    elif self.blocks[block] == "S - spawner":
                        self.entities.append(Spawner(self.win, (x * self.ssw) + self.offset[0], (y * self.ssh) + self.offset[1], x, y, self.ssw, self.ssh, self.textures["Blocks"]["spawner"]))

                    elif self.blocks[block].starts_with("S - player"):
                        self.entities.append(Player(self.win, (x * self.ssw) + self.offset[0], (y * self.ssh) + self.offset[1], self.ssw, self.ssh, x, y, self.textures["Players"][self.blocks[block][-1:]]["0"], self.textures["Blocks"]["projectile"], self.textures["Players"], self.players[int(self.blocks[block][-1:]) - 1], (200, 0, 0) if self.blocks[block][-1:] == "1" else (0, 200, 0) if self.blocks[block][-1:] == "2" else (0, 0, 200) if self.blocks[block][-1:] == "3" else (200, 200, 0), [self.offset[0], self.offset[1], self.ws["w"] // 8, self.ws["h"] // 10] if self.blocks[block][-1:] == "1" else [self.offset[0] + (self.ws["w"] - (self.ws["w"] // 8)), self.offset[1], self.ws["w"] // 8, self.ws["h"] // 10] if self.blocks[block][-1:] == "2" else [self.offset[0], self.offset[1] + (self.ws["h"] - (self.ws["h"] // 10)), self.ws["w"] // 8, self.ws["h"] // 10] if self.blocks[block][-1:] == "3" else [self.offset[0] + (self.ws["w"] - (self.ws["w"] // 8)), self.offset[1] + (self.ws["h"] - (self.ws["h"] // 10)), self.ws["w"] // 8, self.ws["h"] // 10], 0, map["stats"]["health"], map["stats"]["ammo"], self.blocks[block][-1:]))

                    
                else:
                    image = self.textures["Blocks"][self.blocks[block]]["0"]

                self.data[y][x] = {"image": pygame.transform.scale(image, (self.ssw, self.ssh)), "texture": image}

    def draw(self):
        for y in range(len(self.data)):
            for x in range(len(self.data[y])):
                block = self.data[y][x]["image"]
                
                self.win.blit(block, ((self.ssw * x) + self.offset[0], (self.ssh * y) + self.offset[1]))
        
        for entity in self.entities:
            entity.draw()

    def resize(self, win, w=None, h=None):
        self.win = win

        if w != None and h != None:
            self.ws = {"w": w, "h": h}
        else:
            self.ws = {"w": win.get_width(), "h": win.get_height()}

        if self.corr:
            self.ssw = self.ws["w"] // len(self.data[0])
            self.ssh = self.ws["h"] // len(self.data)
            if self.ssw < self.ssh:
                self.offset = [0, (self.ws["h"] - self.ssw * len(self.data)) // 2]
                self.ws = {"w": self.win.get_width(), "h": self.ssw * len(self.data)}

            elif self.ssw > self.ssh:
                self.offset = [(self.ws["w"] - self.ssh * len(self.data[0])) // 2, 0]
                self.ws = {"w": self.ssh * len(self.data[0]), "h": self.win.get_height()}

            self.rect = [self.offset[0], self.offset[1], self.ws["w"], self.ws["h"]]

        self.ssw = self.ws["w"] // len(self.data[0])
        self.ssh = self.ws["h"] // len(self.data)

        for y in range(len(self.data)):
            for x in range(len(self.data[y])):
                self.data[y][x]["image"] = pygame.transform.scale(self.data[y][x]["texture"], (self.ssw, self.ssh))

        for entity in self.entities:
            if isinstance(entity, Player):
                entity.resize(self.win, self.ssw, self.ssh, self.rect, [self.offset[0], self.offset[1], self.ws["w"] // 8, self.ws["h"] // 10] if entity.id == "1" else [self.offset[0] + (self.ws["w"] - (self.ws["w"] // 8)), self.offset[1], self.ws["w"] // 8, self.ws["h"] // 10] if entity.id == "2" else [self.offset[0], self.offset[1] + (self.ws["h"] - (self.ws["h"] // 10)), self.ws["w"] // 8, self.ws["h"] // 10] if entity.id == "3" else [self.offset[0] + (self.ws["w"] - (self.ws["w"] // 8)), self.offset[1] + (self.ws["h"] - (self.ws["h"] // 10)), self.ws["w"] // 8, self.ws["h"] // 10])
            else:
                entity.resize(self.win, self.ssw, self.ssh, self.rect)

    def update(self):
        for i in self.entities:
            if isinstance(i, Spawner):
                i.update()

            


#[self.offset[0], self.offset[1], self.ws["w"] // 8, self.ws["h"] // 10] if entity.id == "1" else [self.offset[0] + (self.ws["w"] - (self.ws["w"] // 8)), self.offset[1], self.ws["w"] // 8, self.ws["h"] // 10] if entity.id == "2" else [self.offset[0], self.offset[1] + (self.ws["h"] - (self.ws["h"] // 10)), self.ws["w"] // 8, self.ws["h"] // 10] if entity.id == "3" else [self.offset[0] + (self.ws["w"] - (self.ws["w"] // 8)), self.offset[1] + (self.ws["h"] - (self.ws["h"] // 10)), self.ws["w"] // 8, self.ws["h"] // 10]