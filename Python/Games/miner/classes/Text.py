import pygame

class Text:
    def __init__(self, x, y, size, text, color=(0, 0, 0)):
        self.x = x
        self.y = y
        self.size = size
        self.text = text
        self.color = color
        self.font = pygame.font.Font(None, self.size)
        self.render_text = self.font.render(self.text, True, self.color)
        
    def draw(self, win):
        win.blit(self.render_text, (self.x, self.y))