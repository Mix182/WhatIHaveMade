import pygame, time

from .Projectile import Projectile

class Spawner:
    def __init__(self, win, x, y, in_grid_x, in_grid_y, w, h, texture, full_generate_time=10.0):
        self.win = win
        self.x = x
        self.y = y
        self.w = w
        self.h = h
        self.txt = texture
        self.igx = in_grid_x
        self.igy = in_grid_y

        self.slot = None

        self.fgt = full_generate_time

        self.time = time.time()

        self.img = "unloaded"

        self.construct()

    def construct(self):
        self.images = {}
        
        for x in self.txt:
            self.images[x] = pygame.transform.scale(self.txt[x], (self.w, self.h))
                

        self.sgt = self.fgt / (len(self.images) - 2)

    def draw(self):
        self.win.blit(self.images[self.img], (self.x, self.y))

    def resize(self, win, ssw, ssh, grid_rect=[]):
        self.win = win

        if grid_rect == []:
            self.w = ssw
            self.h = ssh
            self.x = (self.igx * self.w)
            self.y = (self.igy * self.h)

        else:
            self.w = ssw
            self.h = ssh
            self.x = (self.igx * self.w) + grid_rect[0]
            self.y = (self.igy * self.h) + grid_rect[1]

        self.construct()

    def update(self):
        diferentses = time.time() - self.time
        if diferentses > self.sgt:
            try:
                img = int(self.img)
            except Exception:
                if self.img == "unloaded":
                    img = 0

                elif self.img == "loaded":
                    img = int(len(self.images))

            if not img >= len(self.images) - 2:
                self.img = str(int(diferentses // self.sgt))

            else:
                self.img = "loaded"
