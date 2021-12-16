import pygame

class Railway:
    def __init__(self, win, x, y, in_grid_x, in_grid_y, w, h, textures, inputs):
        self.win = win
        self.x = x
        self.y = y
        self.w = w
        self.h = h
        self.txt = textures
        self.inputs = inputs
        self.igx = in_grid_x
        self.igy = in_grid_y

        self.construct()

    def construct(self):
        #curved_in (bigger part), curved_out (smaller part), straight
        inp = self.inputs
        self.images = []

        ci = self.txt["curved_in"]
        co = self.txt["curved_out"]
        s  = self.txt["straight"]

        if "up" in inp:
            if "left" in inp:
                img = pygame.transform.scale(ci, (self.w // 2, self.h // 2))

            else:
                img = pygame.transform.scale(pygame.transform.rotate(s, 90), (self.w // 2, self.h // 2))

            if "right" in inp:
                img2 = pygame.transform.scale(pygame.transform.rotate(ci, 270), (self.w // 2, self.h // 2))

            else:
                img2 = pygame.transform.scale(pygame.transform.rotate(s, 270), (self.w // 2, self.h // 2))


        else:
            if "left" in inp:
                img = pygame.transform.scale(s, (self.w // 2, self.h // 2))
                
            else:
                img = pygame.transform.scale(co, (self.w // 2, self.h // 2))

            if "right" in inp:
                img2 = pygame.transform.scale(s, (self.w // 2, self.h // 2))
                
            else:
                img2 = pygame.transform.scale(pygame.transform.rotate(co, 270), (self.w // 2, self.h // 2))
        
        self.images.append({"image": img, "pos": [self.x, self.y]})
        self.images.append({"image": img2, "pos": [self.x + self.w // 2, self.y]})

        if "down" in inp:
            if "left" in inp:
                img = pygame.transform.scale(pygame.transform.rotate(ci, 90), (self.w // 2, self.h // 2))

            else:
                img = pygame.transform.scale(pygame.transform.rotate(s, 90), (self.w // 2, self.h // 2))

            if "right" in inp:
                img2 = pygame.transform.scale(pygame.transform.rotate(ci, 180), (self.w // 2, self.h // 2))

            else:
                img2 = pygame.transform.scale(pygame.transform.rotate(s, 270), (self.w // 2, self.h // 2))


        else:
            if "left" in inp:
                img = pygame.transform.scale(pygame.transform.rotate(s, 180), (self.w // 2, self.h // 2))
                
            else:
                img = pygame.transform.scale(pygame.transform.rotate(co, 90), (self.w // 2, self.h // 2))

            if "right" in inp:
                img2 = pygame.transform.scale(pygame.transform.rotate(s, 180), (self.w // 2, self.h // 2))

            else:
                img2 = pygame.transform.scale(pygame.transform.rotate(co, 180), (self.w // 2, self.h // 2))
        
        self.images.append({"image": img, "pos":  [self.x, self.y + self.h // 2]})
        self.images.append({"image": img2, "pos": [self.x + self.w // 2, self.y + self.h // 2]})

        #print(self.igx, self.igy, inp)

    def draw(self):
        for i in self.images:
            self.win.blit(i["image"], i["pos"])

    def resize(self, win, ssw, ssh, grid_rect=[]):
        self.win = win

        if grid_rect == []:
            self.w = ssw
            self.h = ssh
            self.x = (self.igx * self.w)
            self.y = (self.igy * self.h)

        else:
            self.w = ssw
            self.h = ssh
            self.x = (self.igx * self.w) + grid_rect[0]
            self.y = (self.igy * self.h) + grid_rect[1]

        self.construct()
