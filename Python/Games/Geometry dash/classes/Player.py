import pygame

class Player:
    def __init__(self, x, y, win, speed, color = (100, 100, 100), width = 50, height = 50):
        self.win = win
        self.rect = pygame.Rect(x, y, width, height)
        self.mid_air = False
        self.y_motion = 0
        self.colision_tolerance = speed
        self.speed = speed
        self.color = color
        
    def move(self, space_presed):
        if space_presed and not self.mid_air:
            self.mid_air = True
            self.y_motion = 15
        
        touched = self.touching(blocks)
        if self.mid_air:
            self.rect.y -= self.y_motion
            self.y_motion -= 1
            if touched[1]:
                self.y_motion = 0
                self.mid_air = False
                
        if not touched[1] and not self.mid_air:
            self.mid_air = True
            self.y_motion = 0 
         
            
    def update(self, blocks):
        touched = self.touching(blocks)
        if touched[0]:
            self.die()
            
        if touched[2]:
            self.die()
        
        if touched[3]:
            self.die()
            
    def touching(self, thinks):
        touched = [False, False, False, False]
        for i in thinks:
            if self.rect.coliderect(i):
                if abs(i.top - self.rect.bottom) < self.colision_tolerance:
                    touched[0]
                    
                if abs(i.bottom - self.rect.top) < self.colision_tolerance:
                    touched[1]
                      
                if abs(i.left - self.rect.right) < self.colision_tolerance:
                    touched[2]
                    
                if abs(i.right - self.rect.left) < self.colision_tolerance:
                    touched[3]
                    
        return touched
                    
    def die(self):
        pass
    
    def draw(self):
        pygame.draw.rect(self.win, self.color, self.rect)