import pygame, random 

class Block:
    def __init__(self, win, x, y, w, h, textures, name, visible=True):
        self.win = win
        self.x = x
        self.y = y
        self.w = w
        self.h = h
        self.image = random.choice(list(textures[name].items()))[1]
        self.resize(w, h)
        self.name = name
        self.visible = visible

    def resize(self, w, h):
        self.image = pygame.transform.scale(self.image, (w, h))

        self.w = w
        self.h = h

    def draw(self):
        if self.visible:
            self.win.blit(self.image, (self.x, self.y))

        else:
            pygame.draw.rect(self.win, (0, 0, 0), (self.x, self.y, self.w, self.h))

    