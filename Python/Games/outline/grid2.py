import pygame

class Grid:
    def __init__(self, win, square_count_x, square_count_y, data=[], color=(0, 0, 0), alpha=100):
        self.win = win
        self.sw = win.get_width() // square_count_x #square width
        self.sh = win.get_height() // square_count_y #square height
        self.scx = square_count_x
        self.scy = square_count_y
        self.data = data
        self.c = color
        self.a = alpha

    def update(self, win, square_count_x, square_count_y):
        self.win = win

        if (square_count_x < 1 or square_count_y < 1) or (square_count_x > win.get_width() // 10 or square_count_y > win.get_height() // 10):
            return
        
        self.scx = square_count_x
        self.scy = square_count_y
        self.sw = win.get_width() // self.scx
        self.sh = win.get_height() // self.scy

    def place(self, mouse_pos): #change place
        pos = {"x": mouse_pos[0] // self.sw, "y": mouse_pos[1] // self.sh, "c": self.c}

        if not pos in self.data:
            self.data.append(pos)

    def destroy(self, mouse_pos):
        pos = {"x": mouse_pos[0] // self.sw, "y": mouse_pos[1] // self.sh, "c": self.c}

        if pos in self.data:
            self.data.remove(pos)

    def clear(self):
        self.data = []

    def draw(self):
        w = self.sw // 20
        h = self.sh // 20
        
        for i in self.data:
            x = i["x"]
            y = i["y"]
            if not (x * self.sw > self.win.get_width() or y * self.sh > self.win.get_height()):
                surface = pygame.Surface((self.sw, self.sh))
                surface.fill(i["c"])
                surface.set_alpha(self.a)
                self.win.blit(surface, (i["x"] * self.sw, i["y"] * self.sh))

        for i in self.data:
            x = i["x"]
            y = i["y"]
            c = i["c"]

            if not (x * self.sw > self.win.get_width() or y * self.sh > self.win.get_height()):
                if not {"x": x, "y": y-1, "c": c} in self.data:
                    pygame.draw.rect(self.win, c, ((x * self.sw) - (w // 2), (y * self.sh) - (h // 2), self.sw + w, h))
                
                if not {"x": x, "y": y+1, "c": c} in self.data:
                    pygame.draw.rect(self.win, c, ((x * self.sw) - (w // 2), ((y + 1) * self.sh) - (h // 2), self.sw + w, h))

                if not {"x": x-1, "y": y, "c": c} in self.data:
                    pygame.draw.rect(self.win, c, ((x * self.sw) - (w // 2), (y * self.sh) - (h // 2), w, self.sh + h))

                if not {"x": x+1, "y": y, "c": c} in self.data:
                    pygame.draw.rect(self.win, c, (((x + 1) * self.sw) - (w // 2), (y * self.sh) - (h // 2), w, self.sh + h))


       

        