import pygame

class Image:
    def __init__(self, win, x, y, w, h, image, scene=None):
        self.win = win
        self.x = x
        self.y = y
        self.w = w
        self.h = h
        self.i = pygame.image.scale(image, (w, h))
        self.img = image
        self.scene = scene
    
    def resize(self, win, x, y, w, h):
        self.win = win
        self.x = x
        self.y = y
        self.w = w
        self.h = h

        self.i = pygame.image.scale(self.img, (w, h))

    def draw(self):
        self.win.blit(self.i, (self.x, self.y))

        