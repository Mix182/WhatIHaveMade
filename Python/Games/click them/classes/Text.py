import pygame
pygame.font.init()

class Text:
    def __init__(self, x, y, size, text, win, color=(0, 0, 0)):
        self.x = x
        self.y = y
        self.size = size
        self.text = text
        self.color = color
        self.font = pygame.font.Font(None, self.size)
        self.render_text = self.font.render(self.text, True, self.color)
        self.win = win
        
    def draw(self):
        self.win.blit(self.render_text, (self.x, self.y))
        
    def change_text(self, text):
        self.text = text
        self.render_text = self.font.render(self.text, True, self.color)