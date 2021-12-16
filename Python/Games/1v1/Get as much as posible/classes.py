import pygame, random
from pygame.locals import *
pygame.init()

class Text_box:
    def __init__(self, x, y):
        self.text = ""
        self.x = x
        self.y = y
        self.blit_text = Text(self.x, self.y, 32, self.text)
        
    def update(self, event):
        if event.type == KEYDOWN:
            if event.key == K_BACKSPACE:
                self.text = text[: -1]
            else:
                self.text += event.unicode
                    
    def draw(self, win):
        self.blit_text.draw(win)

class Button:
    def __init__(self, x, y, width, height, color, text):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.color = color
        self.text = text
        self.blit_text = Text(self.x + self.width / 10, self.y + self.height / 10, 96, self.text)
        
    def draw(self, win):
        pygame.draw.rect(win, self.color, (self.x, self.y, self.width, self.height), 0)
        self.blit_text.draw(win)
        
    def is_touching(self, mouse_pos):
        if mouse_pos[0] > self.x and mouse_pos[0] < self.x + self.width:
            if mouse_pos[1] > self.y and mouse_pos[1] < self.y + self.height:
                return True
            
        return False 
    
class Player:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.speed = 2
        self.points = 0
        self.moving_up = False
        self.moving_down = False
        self.moving_right = False
        self.moving_left = False
        self.color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
        
    def draw(self, win):
        pygame.draw.circle(win, (0, 0, 0), (self.x, self.y), self.points + 8)
        pygame.draw.circle(win, self.color, (self.x, self.y), self.points + 5)
        
    def move(self):
        self.speed = 10 // (self.points + 1)
        
        if self.speed < 2:
            self.speed = 2
        
        if self.moving_up:
            self.y -= self.speed
            
        if self.moving_down:
            self.y += self.speed
        
        if self.moving_right:
            self.x += self.speed
            
        if self.moving_left:
            self.x -= self.speed
    
class Text:
    def __init__(self, x, y, size, text):
        self.x = x
        self.y = y
        self.size = size
        self.text = text
        self.font = pygame.font.Font(None, self.size)
        self.render_text = self.font.render(self.text, True, (0, 0, 0))
        
    def draw(self, win):
        win.blit(self.render_text, (self.x, self.y))
    
class Point():
    def __init__(self, win_size):
        self.chose_random(win_size)
    
    def chose_random(self, win_size):
        self.pos = (random.randint(0, win_size[0]), random.randint(0, win_size[1]))
        self.points = random.randint(2, 5)
        self.color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
        self.r = self.points * 2
        
    def draw(self, win):
        pygame.draw.circle(win, self.color, self.pos, self.r)
        
    def is_touching(self, player, win_size):
        if self.calc_dist(player) <= player.points + 5:
            player.points += self.points // 3
            self.chose_random(win_size)

    def calc_dist(self, pos2):
        if self.pos[0] == pos2.x:
            a = self.pos[0] - pos2.x
            return (a ** 2) ** 0.5
        
        if self.pos[1] == pos2.y:
            a = self.pos[1] - pos2.y
            return (a ** 2) ** 0.5
        
        a = ((self.pos[0] - pos2.x) ** 2) ** 0.5
        b = ((self.pos[1] - pos2.y) ** 2) ** 0.5
        c = ((a ** 2) + (b ** 2)) ** 0.5

        return c

