# Importing some stuff
import pygame, sys, os, random
from pygame.locals import *

# Initilazing
pygame.init()
clock = pygame.time.Clock()

# Seting up screen
win_size = (800, 800)
win = pygame.display.set_mode(win_size, 0, 32)
pygame.display.set_caption("Get out of here")

class Button():
    def __init__(self, color, x,y,width,height, text=''):
        self.color = color
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.text = text

    def draw(self,win,outline=None):
        #Call this method to draw the button on the screen
        if outline:
            pygame.draw.rect(win, outline, (self.x-2,self.y-2,self.width+4,self.height+4),0)
            
        pygame.draw.rect(win, self.color, (self.x,self.y,self.width,self.height),0)
        
        if self.text != '':
            font = pygame.font.SysFont('consolas', 60)
            text = font.render(self.text, 1, (0,0,0))
            win.blit(text, (self.x + (self.width/2 - text.get_width()/2), self.y + (self.height/2 - text.get_height()/2)))

    def isOver(self, pos):
        #Pos is the mouse position or a tuple of (x,y) coordinates
        if pos[0] > self.x and pos[0] < self.x + self.width:
            if pos[1] > self.y and pos[1] < self.y + self.height:
                return True
            
        return False
        
class Enemies():
    def __init__(self, count):
        self.count = count
        self.x = 0
        self.y = -40
        self.width = 40
        self.hright = 40
        self.positions = []
        self.select_random()
        
    def select_random(self):
        self.positions.clear()
        
        for i in range(self.count):
            self.positions.append(random.randint(0, win_size[0] - self.width))

    def draw(self, win):
        for i in range(len(self.positions)):
            self.x = self.positions[i]
            pygame.draw.rect(win, (200, 100, 200), (self.x, self.y, self.width, self.hright))
            
    def move(self, speed, win, player):
        self.y += speed
        
        if self.y > win_size[1]:
            self.select_random()
            self.draw(win)
            self.y = 0
        
"""
    def touching(self, py, px):
        if py < self.y and py + 50 > self.y + self.width:
            for enemy in self.positions:
                if px < enemy

        else:
            return False
"""
class Player():
    def __init__(self):
        self.x = 400
        self.y = 700
        self.width = 50 # Šířka
        self.height = 50 # Výška
        
    def move_right(self, speed):
        self.x += speed
        
        if self.x > win_size[0] - self.width:
            self.x -= speed

    def move_left(self, speed):
        self.x -= speed
        
        if self.x < 0:
            self.x += speed
        
    def draw(self, win):
        pygame.draw.rect(win, (100, 100, 100), (self.x, self.y, self.width, self.height))



def loby(win):
    run = True
    start_button = Button((100, 255, 100), 300, 400, 200, 75, "Start")
    quit_button = Button((100, 255, 100), 300, 400, 200, 75, "quit")

    while run:
        redraw_loby(win, start_button)
        # Quiting game 
        for event in pygame.event.get():
            mouse_pos = pygame.mouse.get_pos()
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
                run = False
                
            if event.type == MOUSEBUTTONDOWN:
                if start_button.isOver(mouse_pos):
                    run = False
                    game()

def redraw_loby(win, start_button):
    win.fill((100, 100, 100))

    start_button.draw(win, (0, 0, 0))
    
    pygame.display.update()
    clock.tick(60)


def game():
    moving_left = False
    moving_right = False
    
    enemies = Enemies(10)
    player = Player()
    run = True
    
    while run:
        redraw_game(win, player, enemies)
        # Quiting game 
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
                run = False
            if event.type == KEYDOWN:
                if event.key == K_a or event.key == K_LEFT:
                    moving_left = True
                            
                if event.key == K_d or event.key == K_RIGHT:
                    moving_right = True
                            
            if event.type == KEYUP:
                if event.key == K_a or event.key == K_LEFT:
                    moving_left = False
                            
                if event.key == K_d or event.key == K_RIGHT:
                    moving_right = False
                            
        if moving_left == True:
            player.move_left(10)
                    
        if moving_right == True:
            player.move_right(10)
            
def redraw_game(win, player, enemies):
    win.fill((0, 0, 0))
    
    player.draw(win)
    enemies.move(10, win, player)
    enemies.draw(win)
    
    pygame.display.update()
    clock.tick(60)

        
loby(win)