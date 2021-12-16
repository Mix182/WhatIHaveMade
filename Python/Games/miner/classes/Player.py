import pygame

class Player:
    def __init__(self, win, textures, w, h, grid=None):
        self.win = win
        self.txtrs = textures
        self.state = len(textures) - 1
        self.mooving = False
        self.resize(w, h)
        self.falling = 0
        self.grid = grid
        self.gx = 0
        self.gy = 0

    def draw(self):
        self.win.blit(self.txtrs[str(self.state)], (self.x, self.y))

    def resize(self, w, h):
        for i in self.txtrs:
            self.txtrs[i] = pygame.transform.scale(self.txtrs[i], (w, h))

        self.x = (self.win.get_width() / 2) - (w / 2)
        self.y = (self.win.get_height() / 2) - (h / 2)

    def move(self, key):
        if not self.mooving:
            self.mooving = key

