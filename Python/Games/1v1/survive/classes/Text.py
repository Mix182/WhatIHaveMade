import pygame

class Text:
    def __init__(self, win, x, y, size, text, color=(0, 0, 0), scene=None):
        self.win = win
        self.x = x
        self.y = y
        self.size = size
        self.text = text
        self.color = color
        self.scene = scene
        self.font = pygame.font.Font("/home/pi/Desktop/Programování/Python/Projekty/My games/1v1/survive/assets/font/PixelMplus10-Regular.ttf", self.size)
        self.render_text = self.font.render(self.text, True, self.color)
        
    def draw(self):
        self.win.blit(self.render_text, (self.x, self.y))

    def resize(self, win, x, y, size):
        self.win = win
        self.x = x
        self.y = y
        self.size = size

        self.font = pygame.font.Font("/home/pi/Desktop/Programování/Python/Projekty/My games/1v1/survive/assets/font/PixelMplus10-Regular.ttf", self.size)
        self.render_text = self.font.render(self.text, True, self.color)

    def change_text(self, new_text):
        self.text = new_text
        self.render_text = self.font.render(new_text, True, self.color)