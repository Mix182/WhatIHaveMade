import pygame

from classes import *
from pygame.locals import *

pygame.init()

win_size = [800, 800]

clock = pygame.time.Clock()
win = pygame.display.set_mode(win_size)

pygame.display.set_caption("Tik Tak Toe")

def main(win, clock):
    lobby(win, clock)
    x, count = chosing_level(win, clock)
    game(win, clock, x, count)

def lobby(win, clock):
    play_button = Button(300, 350, 200, 100, (0, 255, 0), "PLAY", 90)
    quit_button = Button(300, 500, 200, 100, (255, 0, 0), "QUIT", 90)
    
    run = True
    while run:
        mouse_pos = pygame.mouse.get_pos()
        for event in pygame.event.get():
            if event.type == QUIT:
                run = False
                pygame.quit()
                quit()
                
            if event.type == MOUSEBUTTONDOWN:
                if play_button.is_touching(mouse_pos):
                    run = False
                    
                if quit_button.is_touching(mouse_pos):
                    run = False
                    pygame.quit()
                    quit()
                
        redraw(win, (100, 100, 100), clock, [play_button, quit_button])

def chosing_level(win, clock):
    text = Text(100, 200, 96, "Type scale of grid")
    runed = 0
    
    players_input = ""
    
    run = True
    while run:
        for event in pygame.event.get():
            if event.type == QUIT:
                run = False
                pygame.quit()
                quit()
                
            if event.type == KEYDOWN:
                if event.key == K_BACKSPACE:
                    players_input = players_input[: -1]
                
                elif event.key == K_RETURN:
                    text = Text(100, 200, 96, "Type the next think")
                    if runed == 0:
                        x = int(players_input)
                        runed = 1
                        players_input = ""
                        
                    else:
                        count = players_input
                        return x, count
                else:
                    players_input += event.unicode
                    if not players_input == "":
                        if int(players_input) > 50:
                            players_input = "50"
                   
                    
        players_text = Text(350, 400, 96, players_input)
        redraw(win, (255, 255, 255), clock, [text, players_text])
def game(win, clock, x, count):
    grid = make_grid(x)
    
    squer_size = win.get_width() // len(grid)
    
    now_playing = "o"
    
    run = True
    while run:
        mouse_pos = pygame.mouse.get_pos()
        
        for event in pygame.event.get():
            if event.type == QUIT:
                run = False
                pygame.quit()
                quit()
                
            if event.type == MOUSEBUTTONDOWN:
                if grid[mouse_pos[0] // squer_size][mouse_pos[1] // squer_size] == "":
                    grid[mouse_pos[0] // squer_size][mouse_pos[1] // squer_size] = now_playing
                    if now_playing == "o":
                        now_playing = "x"
                    
                    elif now_playing == "x":
                        now_playing = "o"
        symbols_in_line = 0               
                    
                
        redraw_game(win, clock, grid, squer_size)

def redraw_game(win, clock, grid, squer_size):
    win.fill((255, 255, 255))
    
    for i in range(len(grid)):
        pygame.draw.line(win, (0, 0, 0), (i * squer_size, win.get_width()), (i * squer_size, 0), 5)
        for j in range(len(grid[i])):
            pygame.draw.line(win, (0, 0, 0), (win.get_width(), i * squer_size), (0, i * squer_size), 5)
            
            if grid[i][j] == "x":
               pygame.draw.line(win, (0, 0, 255), ((i * squer_size) + (squer_size // 10), (j * squer_size) + (squer_size // 10)), ((i * squer_size) + 9 * (squer_size // 10), (j * squer_size) + 9 * (squer_size // 10)), squer_size // 10)
               pygame.draw.line(win, (0, 0, 255), ((i * squer_size) + 9 * (squer_size // 10), j * squer_size + (squer_size // 10)), (i * squer_size  + (squer_size // 10), j * squer_size + 9 * (squer_size // 10)), squer_size // 10) 
            
            elif grid[i][j] == "o":
                pygame.draw.circle(win, (255, 0, 0), (i * squer_size + squer_size // 2, j * squer_size + squer_size // 2), 4 * (squer_size // 10), squer_size // 10)
                
    pygame.display.update()
    clock.tick(60)

def make_grid(x):
    grid = []
    for i in range(x):
        grid.append([])
        for j in range(x):
            grid[i].append("")
    return grid

def redraw(win, BG_color, clock, things = []):
    win.fill(BG_color)
    for i in range(len(things)):
        things[i].draw(win)
        
    pygame.display.update()
    clock.tick(60)
    
main(win, clock)
    