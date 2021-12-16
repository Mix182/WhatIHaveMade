import pygame
class Block:
    def __init__(self, y, x, v, m, w, c):
        self.y = y
        self.x = x
        self.v = v
        self.m = m
        self.w = w
        self.c = c

    def draw(self, win):
        pygame.draw.rect(win, self.c, (self.x, self.y - self.w, self.w, self.w))