import pygame, random
from noise import pnoise2, snoise2

class Map:
    def __init__(self, win, grid_size, colors=[]):
        self.win = win
        self.grid_size = grid_size
        self.win_size = [win.get_width(), win.get_height()]
        self.block_size = [win.get_width() // grid_size[0], win.get_height() // grid_size[1]]
        self.colors = colors
        self.offset = [0, 0]
        self.zoom = 10.0
        self.generate()

    def generate(self, offset=[0,0], zoom=0.0):
        self.data = [[r for r in range(self.grid_size[0])] for i in range(self.grid_size[1])]
        
        if offset == self.offset and zoom == 0.0:
            self.offset = [0, 0] #[int(random.random() * (10 ** 5)), int(random.random() * (10 ** 5))]
            print(f"offset: {self.offset}")

        else:
            self.offset = offset

        if zoom > 0.0:
            self.zoom *= zoom

        elif zoom < 0.0:
            self.zoom /= (zoom * -1)

        for y in range(self.grid_size[1]):
	        for x in range(self.grid_size[0]):
		        self.data[x][y] = int(snoise2((x + self.offset[0]) / self.zoom, (y + self.offset[1]) / self.zoom, octaves=2, persistence=10.0) * 127.0 + 128.0)

    def draw(self):
        for y in range(len(self.data)):
            for x in range(len(self.data[y])):
                pixel = self.data[x][y]
                if self.colors == []:
                    color = (pixel, pixel, pixel)

                else:
                    for i in self.colors:
                        if pixel >= i[0] and pixel <= i[1]:
                            color = i[2]
                            continue
                
                pygame.draw.rect(self.win, color, (x * self.block_size[0], y * self.block_size[1], self.block_size[0], self.block_size[1]))


    def change_block(self, mouse_pos):
        pass

    def change_selected(self, to, speed=10):
        self.speed = speed
        if to == "r":
            self.generate()
        elif to == "<":
            self.generate([self.offset[0] - self.speed, self.offset[1]])
        elif to == ">":
            self.generate([self.offset[0] + self.speed, self.offset[1]])
        elif to == "^":
            self.generate([self.offset[0], self.offset[1] - self.speed])
        elif to == "v":
            self.generate([self.offset[0], self.offset[1] + self.speed])
        elif to == "^^":
            self.generate(offset=self.offset, zoom=-2)
        elif to == "vv":
            self.generate(offset=self.offset, zoom=2)

    def resize(self):
        pass