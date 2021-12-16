import pygame

from .Text import Text

class Player:
    def __init__(self, win, x, y, w, h, igx, igy, texture, projectile_textures, health_textures, name, color, hud=[0, 0, 100, 100], degree=0, max_health=3, max_projectiles=3, id=1):
        self.win = win
        self.x = x
        self.y = y
        self.w = w
        self.h = h
        self.igx = igx
        self.igy = igy
        self.deg = degree
        self.txt = texture
        self.p_txt = projectile_textures
        self.h_txt = health_textures
        self.hud = hud
        self.name = name
        self.color = color

        self.id = id

        self.health = max_health
        self.mh = max_health

        self.projectiles = 0
        self.mp = max_projectiles

    def make(self, hud=True):
        self.img = pygame.transform.scale(pygame.transform.rotate(self.txt, self.deg), [self.w, self.h])
            
        if hud:
            self.hud_items = []
            x, y, w, h, = self.hud
            spacing = w // 20

            self.hud_items.append(Text(self.win, 0, self.y, (h // 3) - spacing, self.name, self.color))
            self.hud_items[0].x = x + ((w // 2) - (self.hud_items[0].render_text.get_width() // 2))

            for i in range(self.mh):
                self.hud_items.append([[x + ((w // self.mh) * i), y + (h // 3)], pygame.transform.scale(self.h_txt["heart_full" if self.health > i else "heart_empty"], ((w // self.mh) - spacing), (h // 3) - spacing)])

            for i in range(self.mp):
                self.hud_items.append([[x + ((w // self.mp) * i), y + ((h // 3) * 2)], pygame.transform.scale(self.p_txt["hud_full" if self.projectiles > i else "hud_empty"], ((w // self.mp) - spacing), (h // 3) - spacing)])

    def draw(self):
        self.win.blit((self.x, self.y), self.img)
        
        for i in self.hud_items:
            try:
                i.draw()

            except Exception:
                self.win.blit(i[0], i[1])

    def rotate(self, deg):
        self.deg = deg
        self.make(hud=False)

    def move_to(self, x, y, igx, igy):
        self.x = x
        self.y = y
        self.igx = igx
        self.igy = igy

    def resize(self, win, w, h, grid_square, hud):
        self.win = win
        self.x = grid_square[0] + (w * self.igx)
        self.y = grid_square[1] + (h * self.igy)
        self.w = w
        self.h = h
        self.hud = hud
        self.make()

    def change(self, health=None, projectiles=None):
        if health != None:
            self.health = health
            self.make()
        
        if projectiles != None:
            self.projectiles = projectiles
            self.make()

