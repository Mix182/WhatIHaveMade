import pygame

from .Text import Text

class Button:
    def __init__(self, win, x, y, w, h, text, images=None, bg_color={"active":(0,255,0),"inactive":(0,100,0),"pressed":(0,50,0)}, outline_color={"active":(0,0,0),"inactive":(0,0,0),"pressed":(0,0,0)}, text_color={"active":(0,0,0),"inactive":(0,0,0),"pressed":(0,0,0)}, scale_on_touch=10, scene=None):
        self.win = win
        self.x = x
        self.y = y
        self.w = w
        self.h = h

        self.images = images

        self.rect = pygame.Rect(x, y, w, h)

        self.a = "inactive"

        if images == None:
            self.i = None
            self.bc = bg_color
            self.tc = text_color
            self.oc = outline_color

        else:
            self.i = {}
            for i in images:
                self.i[i] = pygame.transform.scale(images[i], (w, h))
            self.bc = None
            self.tc = None
            self.oc = None

        self.text = Text(win, 0, 0, int(h * 0.8), text, self.tc[self.a])
        self.text.x = x + ((w // 2) - (self.text.render_text.get_width() // 2))
        self.text.y = y + ((h // 2) - (self.text.render_text.get_height() // 2))

        self.sot = scale_on_touch
        self.scene = scene

    def draw(self):
        if self.i == None:
            if self.bc != None:
                pygame.draw.rect(self.win, self.bc[self.a], self.rect)

            if self.oc != None:
                pygame.draw.rect(self.win, self.oc[self.a], self.rect, self.w // 20)

            self.text.draw()

        else:
            self.win.blit(self.i[self.a], self.rect)

    def resize(self, win, x, y, w, h):
        self.win = win
        self.x = x
        self.y = y
        self.w = w
        self.h = h
        self.rect = pygame.Rect(x, y, w, h)

        self.text.resize(win, 0, y + (h // 2) - ((h * 0.6) // 2), int(h * 0.8))
        self.text.x = x + ((w // 2) - (self.text.render_text.get_width() // 2))
        self.text.y = y + ((h // 2) - (self.text.render_text.get_height() // 2))
        

    def touching(self, mouse_pos):
        x, y, w, h = (self.x, self.y, self.w, self.h)
        if self.rect.collidepoint(mouse_pos):
            if self.a != "active":
                self.a = "active"

                self.rect = pygame.Rect(x - self.sot, y - self.sot, w + (self.sot * 2), h + (self.sot * 2))

                if self.tc != None:
                    self.text.color = self.tc[self.a]
                    self.text.resize(self.win, 0, self.rect.y + (self.rect.h // 2) - ((self.rect.h * 0.6) // 2), int(self.rect.h * 0.8))
                    
                    self.text.x = self.rect.x + ((self.rect.w // 2) - (self.text.render_text.get_width() // 2))
                    self.text.y = self.rect.y + ((self.rect.h // 2) - (self.text.render_text.get_height() // 2))

                if self.i != None:
                    self.i = {}
                    for i in self.images:
                        self.i[i] = pygame.transform.scale(self.images[i], (self.rect.w, self.rect.h))

            return True

        else:
            if self.a != "inactive":
                self.a = "inactive"

                self.rect = pygame.Rect(x, y, w, h)

                if self.tc != None:
                    self.text.color = self.tc[self.a]
                    self.text.resize(self.win, 0, y + (h // 2) - ((h * 0.6) // 2), int(h * 0.8))
                    self.text.x = x + ((w // 2) - (self.text.render_text.get_width() // 2))
                    self.text.y = y + ((h // 2) - (self.text.render_text.get_height() // 2))

                if self.i != None:
                    self.i = {}
                    for i in self.images:
                        self.i[i] = pygame.transform.scale(self.images[i], (self.rect.w, self.rect.h))

            return False
