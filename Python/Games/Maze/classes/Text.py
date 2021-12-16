import pygame

class Text:
    def __init__(self, win, x, y, size, text, color=(0, 0, 0)):
        self.win = win
        self.x = x
        self.y = y
        self.size = size
        self.text = text
        self.color = color
        self.font = pygame.font.Font(None, self.size)
        self.render_text = self.font.render(self.text, True, self.color)
        
    def draw(self):
        self.win.blit(self.render_text, (self.x, self.y))