import pygame

class Map:
    def __init__(self, win, map):
        self.win = win
        self.map = map
        self.lvl = 0
        self.generate_map()

    def generate_map(self):
        self.data = []
        self.laders = []
        ws = [self.win.get_width(), self.win.get_height()]

        scy = len(self.map[self.lvl])
        scx = len(self.map[self.lvl][0])

        self.ssx = ws[0] // scx
        self.ssy = ws[1] // scy

        self.f_lvl = -1

        for y in range(len(self.map[self.lvl])):
            for x in range(len(self.map[self.lvl][y])):
                block = self.map[self.lvl][y][x:x+1]

                if block == " " or block == "#" or block == "S":
                    self.data.append([pygame.Rect(x * self.ssx, y * self.ssy, self.ssx, self.ssy), (0, 0, 0) if block == " " or block == "S" else (100, 100, 100)])
                    if block == "S":
                        self.pr = pygame.Rect((x * self.ssx) + (self.ssx // 4), (y * self.ssy) + (self.ssy // 4), self.ssx // 2, self.ssy // 2)

                elif block == "U" or block == "D" or block == "B":
                    self.laders.append([pygame.Rect(x * self.ssx, y * self.ssy, self.ssx, self.ssy), (200, 200, 0) if block == "U" else (0, 255, 255) if block == "D" else (200, 100, 0)])

                elif block == "F":
                    self.finish = pygame.Rect(x * self.ssx, y * self.ssy, self.ssx, self.ssy)
                    self.f_lvl = self.lvl

    def draw(self):
        for i in self.data:
            pygame.draw.rect(self.win, i[1], i[0])
        
        for i in self.laders:
            pygame.draw.rect(self.win, i[1], i[0])

        if self.f_lvl == self.lvl:
            pygame.draw.rect(self.win, (0, 200, 0), self.finish)

    def colllision(self, rect):
        for i in self.data:
            if i[1] == (100, 100, 100):
                if i[0].colliderect(rect):
                    return True

        if rect.x < 0 or rect.y < 0 or rect.x + rect.w > self.win.get_width() or rect.y + rect.h > self.win.get_height():
            return True

        return False

    def finish_collision(self, rect):

        if self.f_lvl == self.lvl and self.finish.colliderect(rect):
            return True

        else:
            return False

    def resize(self, win):
        self.win = win
        self.generate_map()
        
    def lader_collision(self, rect):
        for i in self.laders:
            if i[0].colliderect(rect):
                if i[1] == (200, 200, 0):
                    return 1

                elif i[1] == (0, 255, 255):
                    return -1

                elif i[1] == (200, 100, 0):
                    return 0
                    
        return False

    def up_level(self, rect):
        if not self.lvl + 1 >= len(self.map):
            self.lvl += 1

            self.generate_map()

            for i in self.laders:
                if i[0].colliderect(rect):
                    if i[1] == (200, 200, 0) or i[1] == (200, 100, 0):
                        return  pygame.Rect(i[0].x + (self.ssx // 4), i[0].y + (self.ssy // 4), self.ssx // 2, self.ssy // 2)
        
        return rect


    def down_level(self, rect):
        if not self.lvl - 1 < 0:
            self.lvl -= 1

            self.generate_map()

            for i in self.laders:
                if i[0].colliderect(rect):
                    if i[1] == (0, 255, 255) or i[1] == (200, 100, 0):
                        return  pygame.Rect(i[0].x + (self.ssx // 4), i[0].y + (self.ssy // 4), self.ssx // 2, self.ssy // 2)

        return rect

