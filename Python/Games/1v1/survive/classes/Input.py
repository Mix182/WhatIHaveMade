from os import scandir
import pygame

from .Text import Text

class Input:
    def __init__(self, win, x, y, w, h, scalable=True, bg_color=None, outline_color={"active": (0, 0, 255), "inactive": (0, 0, 100)}, text_color={"active": (255, 0, 0), "inactive": (100, 0, 0)}, dissabled=False, id=None, scene=None):
        self.win = win
        self.x = x
        self.y = y
        self.w = w
        self.h = h
        self.oc = outline_color
        self.tc = text_color
        self.bc = bg_color
        self.sc = scalable
        self.scene = scene
        self.id = id
        self.width = w
        self.active = False
        self.a = "inactive"
        self.diss = dissabled
        self.text = Text(win, int(x + (w * 0.1)), int(y + (h * 0.1)), int(h * 0.8), "", self.tc[self.a])
        self.text.y = y + ((h // 2) - (self.text.render_text.get_height() // 2))
        self.rect = pygame.Rect(x, y, w, h)

    def draw(self):
        if self.oc != None:
            pygame.draw.rect(self.win, self.oc[self.a], self.rect, self.w // 20)

        if self.bc != None:
            pygame.draw.rect(self.win, self.bc[self.a], self.rect)
        
        self.text.draw()

    def on_click(self, mouse_pos):
        if self.rect.collidepoint(mouse_pos) and not self.diss:
            self.active = True
            self.a = "active"

            self.text.color = self.tc[self.a]

        else:
            self.active = False
            self.a = "inactive"

            self.text.color = self.tc[self.a]

    def resize(self, win, x, y, w, h):
        self.win = win
        self.x = x
        self.y = y
        self.w = w
        self.h = h
        self.rect = pygame.Rect(x, y, w, h)
        self.text.resize(win, int(x + (w * 0.1)), int(y + (h * 0.2)), int(h * 0.8))
        self.text.y = y + ((h // 2) - (self.text.render_text.get_height() // 2))

        if not self.sc:
            while self.text.render_text.get_width() > self.w - (w * 0.1):
                self.text.change_text(self.text.text[:-1])

    def keyboard_input(self, event):
        if self.active:
            if event.key == pygame.K_BACKSPACE:
                self.text.change_text(self.text.text[:-1])

            elif event.key == pygame.K_RETURN:
                self.on_click([self.x - 10, self.y - 10])

            else:
                self.text.change_text(self.text.text + event.unicode)

            if self.sc:
                self.w = max(int(self.text.render_text.get_width() + (self.w // 10)), self.width)
                self.rect.w = self.w + (self.w * 0.1)

            else:
                if self.text.render_text.get_width() > self.w - (self.w * 0.2):
                    self.text.text = self.text.text[:-1]

