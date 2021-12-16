import pygame

class Bullet:
    bullets = []
    
    def __init__(self, win, color, direction, speed, x, y):
        self.win = win
        self.direction = direction
        self.speed = speed
        self.color = color
        Bullet.bullets.append(self)
        self.x = x
        self.y = y
        self.rect = pygame.Rect(self.x, self.y, 10, 20)
    
    def update(self):
        if self.direction == "down":
            self.y += self.speed
            if self.y >= self.win.get_height():
                self.remove()
                
        elif self.direction == "up":
            self.y -= self.speed
            if self.y <= 0:
                self.remove()
                
        self.rect = pygame.Rect(self.x, self.y, 10, 20)
    
    def draw(self):
        if self.direction == "down":
            self.rect.width = 10
            self.rect.height = 20
            pygame.draw.rect(self.win, self.color, self.rect)    
        else:
            self.rect.width = 20
            self.rect.height = 40
            pygame.draw.rect(self.win, self.color, self.rect)
            
    def remove(self):
        Bullet.bullets.remove(self)
    
    @classmethod
    def update_all(cls):
        for i in range(len(cls.bullets)):
            try:
                cls.bullets[i].update()
                
            except Exception:
                pass
    
    @classmethod
    def draw_all(cls):
        for i in range(len(cls.bullets)):
            cls.bullets[i].draw()