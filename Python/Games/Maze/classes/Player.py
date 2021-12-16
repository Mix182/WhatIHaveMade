import pygame

class Player:
    def __init__(self, win, map):
        self.win = win
        self.map = map
        self.rect = map.pr
        self.x_speed = self.rect.w // 3
        self.y_speed = self.rect.h // 3

    def draw(self):
        pygame.draw.rect(self.win, (0, 100, 255), self.rect)

    def resize(self, win):
        self.win = win
        self.rect = self.map.pr
        self.x_speed = self.rect.w // 10
        self.y_speed = self.rect.h // 10

    def update(self, movment):
        #0, 1, 2, 3 = up, down, left, right
        x, y, w, h = self.rect
        if movment[0]:
            if not self.map.colllision(pygame.Rect(x, y - self.y_speed, w, h + self.y_speed)):
                self.rect.y -= self.y_speed
                y = self.rect.y

        if movment[1]:
            if not self.map.colllision(pygame.Rect(x, y, w, h + self.y_speed)):
                self.rect.y += self.y_speed
                y = self.rect.y

        if movment[2]:
            if not self.map.colllision(pygame.Rect(x - self.x_speed, y, w + self.x_speed, h)):
                self.rect.x -= self.x_speed
                x = self.rect.x

        if movment[3]:
            if not self.map.colllision(pygame.Rect(x, y, w + self.x_speed, h)):
                self.rect.x += self.x_speed
            

        return self.map.finish_collision(self.rect)

    def up(self):
        x = self.map.lader_collision(self.rect)
        if x is 1 or x is 0:
            self.rect = self.map.up_level(self.rect)

    def down(self):
        x = self.map.lader_collision(self.rect)
        if x is -1 or x is 0:
            self.rect = self.map.down_level(self.rect)