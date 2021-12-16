import pygame
import random
import time

class Score:
    score = 0
    
    @classmethod
    def reset(cls):
        cls.score = 0
        
    @classmethod
    def add_one(cls):
        cls.score += 1

class Block:
    blocks = []
    score = Score()
    cooldown = 1
    last_spawned = 0
    def __init__(self, win):
        self.win = win
        self.color = (random.randint(10, 255), random.randint(10, 255), random.randint(10, 255))
        width = random.randint(20, 150)
        height = width
        self.rect = pygame.Rect(random.randint(0, self.win.get_width() - width), random.randint(0, self.win.get_height() - height), width, height)
        
    def draw(self):
        pygame.draw.rect(self.win, self.color, self.rect)
        
    def update(self, mouse_pos, mouse_button_down):
        if mouse_button_down and self.is_touching(mouse_pos):    
            Block.score.add_one()
            Block.blocks.remove(self)
        
    def is_touching(self, mouse_pos):
        if mouse_pos[0] > self.rect.x and mouse_pos[0] < self.rect.x + self.rect.width:
            if mouse_pos[1] > self.rect.y and mouse_pos[1] < self.rect.y + self.rect.height:
                return True
        
        else:
            return False
        
    @classmethod
    def new(cls, win):
        if cls.last_spawned + cls.cooldown <= time.time():
            cls.last_spawned = time.time()
            cls.blocks.append(Block(win))
        
    @classmethod
    def draw_all(cls):
        for block in cls.blocks:
            block.draw()
        
    @classmethod
    def update_all(cls, mouse_pos, mouse_button_down):
        for block in cls.blocks:
            block.update(mouse_pos, mouse_button_down)
        
