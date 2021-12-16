import pygame

from .Text import *

class Button:
    def __init__(self, x, y, width, height, color, text, win, size = 96):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.color = color
        self.size = size
        self.text = text
        self.win = win
        self.blit_text = Text(self.x + self.width / 10, self.y + self.height / 10, self.size, self.text)
        
    def draw(self):
        pygame.draw.rect(self.win, self.color, (self.x, self.y, self.width, self.height), 0)
        self.blit_text.draw(self.win)
        
    def is_touching(self, mouse_pos):
        if mouse_pos[0] > self.x and mouse_pos[0] < self.x + self.width:
            if mouse_pos[1] > self.y and mouse_pos[1] < self.y + self.height:
                return True
            
        return False 