import pygame

from .Bullet import Bullet

class Enemy:
    enemies = []
    def __init__(self, win, x, y, color, image):
        self.win = win
        self.x = x
        self.y = y
        self.image = image
        self.color = color
        self.hitbox = pygame.Rect(self.x, self.y, self.image.get_width(), self.image.get_height())
        Enemy.enemies.append(self)
        if self.color == "red":
            self.speed = 5
            self.bullet_speed = 25
            self.color = (255, 0, 0)
            
        elif self.color == "green":
            self.speed = 10
            self.bullet_speed = 20
            self.color = (0, 255 ,0)
            
        elif self.color == "blue":
            self.speed = 15
            self.bullet_speed = 20
            self.color = (0, 0 ,255)
        
    def update(self, bullet):
        self.y += self.speed
        if self.y >= self.win.get_height():
            self.remove()
            
        self.hitbox = pygame.Rect(self.x, self.y, self.image.get_width(), self.image.get_height())
        for i in range(len(bullet.bullets)):
            if self.hitbox.colliderect(bullet.bullets[i].rect) and bullet.bullets[i].direction == "up":
                self.remove()
                bullet.bullets[i].remove()
        
        
    def draw(self):
        self.win.blit(self.image, (self.x, self.y))
        
    def shoot(self):
        self.bullet = Bullet(self.win, self.color, "down", self.bullet_speed, self.x + (self.image.get_width() // 2) - 5, self.y)
        
    def remove(self):
        Enemy.enemies.remove(self)
        
    @classmethod
    def update_all(cls, bullet):
        for i in range(len(cls.enemies)):
            try:
                cls.enemies[i].update(bullet)
            
            except Exception:
                pass
            
    @classmethod
    def shoot_all(cls):
        for i in range(len(cls.enemies)):
            try:
                cls.enemies[i].shoot()
                
            except Exception:
               pass
            
    @classmethod
    def draw_all(cls):
        for i in range(len(cls.enemies)):
            try:
                cls.enemies[i].draw()
                
            except Exception:
                pass