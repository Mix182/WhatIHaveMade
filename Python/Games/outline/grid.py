import pygame

class Grid:
    def __init__(self, win, square_count, win_size):
        self.win = win
        self.sc = square_count
        self.ws = win_size
        self.sw = self.ws[0] // self.sc #square width
        self.sh = self.ws[1] // self.sc #square height
        self.make_grid()
    
    def make_grid(self):
        self.data = []
        for y in range(self.sc):
            self.data.append([])
            for x in range(self.sc):
                self.data[y].append(False)
    
    def ch_place(self, mouse_pos): #change place
        x = mouse_pos[0] // self.sw
        y = mouse_pos[1] // self.sh

        if self.data[y][x]:
            self.data[y][x] = False

        else:
            self.data[y][x] = True

    def draw(self):
        w = self.sw // 20
        h = self.sh // 20

        for y in range(len(self.data)):
            for x in range(len(self.data[y])):
                if self.data[y][x]:
                    pygame.draw.rect(self.win, (0, 122, 255), (x * self.sw, y * self.sh, self.sw, self.sh))
                    try:
                        if not self.data[y-1][x]:
                            pygame.draw.rect(self.win, (0, 0, 0), ((x * self.sw) - (w // 2), (y * self.sh) - (h / 2), self.sw + w, h))
                    except Exception:
                        pygame.draw.rect(self.win, (0, 0, 0), ((x * self.sw) - (w // 2), (y * self.sh) - (h / 2), self.sw + w, h))

                    try:
                        if not self.data[y+1][x]:
                            pygame.draw.rect(self.win, (0, 0, 0), ((x * self.sw) - (w // 2), ((y + 1) * self.sh) - (h / 2), self.sw + w, h))
                    except Exception:
                        pygame.draw.rect(self.win, (0, 0, 0), ((x * self.sw) - (w // 2), ((y + 1) * self.sh) - (h / 2), self.sw + w, h))

                    try:
                        if not self.data[y][x-1]:
                            pygame.draw.rect(self.win, (0, 0, 0), ((x * self.sw) - (h / 2), (y * self.sh) - (w // 2), w, self.sh + h))
                    except Exception:
                        pygame.draw.rect(self.win, (0, 0, 0), ((x * self.sw) - (h / 2), (y * self.sh) - (w // 2), w, self.sh + h))

                    try:
                        if not self.data[y][x+1]:
                            pygame.draw.rect(self.win, (0, 0, 0), (((x + 1) * self.sw) - (h / 2), (y * self.sh) - (w // 2), w, self.sh + h))
                    except Exception:
                        pygame.draw.rect(self.win, (0, 0, 0), (((x + 1) * self.sw) - (h / 2), (y * self.sh) - (w // 2), w, self.sh + h))
