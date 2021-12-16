import pygame
class Wall:
    def __init__(self, y, x, c):
        self.x = x
        self.y = y
        self.c = c

    def draw(self, win):
        pygame.draw.rect(win, self.c, (self.x, 0, 1, self.y))