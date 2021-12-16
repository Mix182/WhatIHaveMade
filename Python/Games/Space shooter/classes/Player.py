import pygame
import time
from .Bullet import *

class Player():
    def __init__(self, win, x, y, image):
        self.x = x
        self.y = y
        self.win = win
        self.image = image
        self.lives = 10
        self.hitbox = pygame.Rect(self.x, self.y, self.image.get_width(), self.image.get_height())
        
    def change_pos(self, x, y):
        self.x = x
        self.y = y
        
    def draw(self):
        self.win.blit(self.image, (self.x, self.y))
        
    def shoot(self):
        self.bullet = Bullet(self.win, (255, 255, 0), "up", 30, self.x + (self.image.get_width() // 2) - 10, self.y)
        
    def update(self, bullet, enemy):
        self.hitbox = pygame.Rect(self.x, self.y, self.image.get_width(), self.image.get_height())
        for i in range(len(bullet.bullets)):
            try:
                if self.hitbox.colliderect(bullet.bullets[i].rect) and bullet.bullets[i].direction == "down":
                    self.lives -= 1
                    bullet.bullets[i].remove()
                    
            except Exception:
                pass
                
        for i in range(len(enemy.enemies)):
            try:
                if self.hitbox.colliderect(enemy.enemies[i].hitbox):
                    self.lives -= 2
                    enemy.enemies[i].remove()
                    
            except Exception:
                pass