import pygame, random

from classes import *
from pygame.locals import *

pygame.init()

win_size = (800, 800)
win = pygame.display.set_mode(win_size)

pygame.display.set_caption("Minesweeper")

def redraw(win, BG_color, draw_stuf = []):
    clock = pygame.time.Clock()
    
    win.fill(BG_color)
    
    for i in range(len(draw_stuf)):
        draw_stuf[i].draw(win)
        
    pygame.display.update()
    clock.tick(60)

def lobby(win):
    BG_color = (200, 255, 200)
    
    start_button = Button(300, 350, 200, 100, (0, 255, 0), "Play")
    quit_button = Button(300, 500, 200, 100, (255, 0, 0), "Quit")
    
    run = True
    while run:
        mouse_pos = pygame.mouse.get_pos()
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                pygame.quit()
                quit()
                
            if event.type == pygame.MOUSEBUTTONDOWN:
                if start_button.is_touching(mouse_pos):
                    run = False
                    
                if quit_button.is_touching(mouse_pos):
                    run = False
                    pygame.quit()
                    quit()
        
        redraw(win, BG_color, [start_button, quit_button])

def dificulty(win):
    BG_color = (200, 255, 200)
    
    easy_button = Button(50, 350, 200, 100, (0, 255, 0), "Easy")
    medium_button = Button(300, 350, 200, 100, (255, 255, 0), "Medium", 60)
    hard_button = Button(550, 350, 200, 100, (255, 0, 0), "Hard")
    
    run = True
    while run:
        
        mouse_pos = pygame.mouse.get_pos()
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                pygame.quit()
                quit()
                
            if event.type == pygame.MOUSEBUTTONDOWN:
                if easy_button.is_touching(mouse_pos):
                    x = 9
                    y = 9
                    mines = 10
                    run = False
                    
                    
                if medium_button.is_touching(mouse_pos):
                    x = 16
                    y = 16
                    mines = 40
                    run = False
                    
                if hard_button.is_touching(mouse_pos):
                    x = 20
                    y = 20
                    mines = 99
                    run = False
                
        redraw(win, BG_color, [easy_button, medium_button, hard_button])
    return [x, y, mines]

def make_grid(x, y):
    grid = []
    
    for i in range(y):
        grid.append([])
        for j in range(x):
            grid[i].append([0, False, False])
            
    return grid
        
def chcose_mines(grid, mines, x, y):
    for i in range(mines):
        grid[random.randint(0, y - 1)][random.randint(0, x - 1)][0] = "mine"
    
    return grid

def update_grid(grid, x, y):
    for i in range(len(grid)):
        for j in range(len(grid[i])):
            if not grid[i][j][0] == "mine":
                mines_around = 0
                
                if not i-1 < 0 and not j-1 < 0:
                    if grid[i-1][j-1][0] == "mine":
                        mines_around += 1
                
                if not i-1 < 0:
                    if grid[i-1][j][0] == "mine":
                        mines_around += 1
                    
                if not i-1 < 0 and not j+1 >= x:    
                    if grid[i-1][j+1][0] == "mine":
                        mines_around += 1
                
                if not j-1 < 0:
                    if grid[i][j-1][0] == "mine":
                        mines_around += 1
                    
                if not j+1 >= x:    
                    if grid[i][j+1][0] == "mine":
                        mines_around += 1
                    
                if not i+1 >= y and not j-1 < 0 :   
                    if grid[i+1][j-1][0] == "mine":
                        mines_around += 1
                
                if not i+1 >= y:
                    if grid[i+1][j][0] == "mine":
                        mines_around += 1
                    
                if not j+1 >= x and not i+1 >= y:
                    if grid[i+1][j+1][0] == "mine":
                        mines_around += 1
                    
                grid[i][j][0] = mines_around
    return grid

def redraw_game(grid, x, y, win_size, squer_size):
    win.fill((255, 255, 255))
    numbers = []
    
    for i in range(x):
        for j in range(y):
            if grid[i][j][1] == False:
                pygame.draw.rect(win, (100, 100, 100), (i * squer_size, j * squer_size, squer_size - 1, squer_size - 1))
                if grid[i][j][2] == True:
                    pygame.draw.rect(win, (0, 255, 0), (i * squer_size + 10, j * squer_size + 10, squer_size - 1 - 20, squer_size - 1 - 20))
                
            elif grid[i][j][1] == True:
                pygame.draw.rect(win, (200, 200, 200), (i * squer_size, j * squer_size, squer_size - 1, squer_size - 1))
                if x > 11:
                    text_size = 32
                    
                else:
                    text_size = 64
                    
                if grid[i][j][0] == "mine":
                    pygame.draw.rect(win, (0, 0, 0), (i * squer_size + 10, j * squer_size + 10, squer_size - 20, squer_size - 20))
                
                elif grid[i][j][0] == 0:
                    pygame.draw.rect(win, (200, 200, 200), (i * squer_size, j * squer_size, squer_size - 1, squer_size - 1))
                
                elif grid[i][j][0] == 1:
                    numbers.append(Text(i * squer_size + squer_size // 4, j * squer_size + squer_size // 4, text_size, str(1), (255, 255, 0)))
                    
                elif grid[i][j][0] == 2:
                    numbers.append(Text(i * squer_size + squer_size // 4, j * squer_size + squer_size // 4, text_size, str(2), (0, 0, 255)))
                    
                elif grid[i][j][0] == 3:
                    numbers.append(Text(i * squer_size + squer_size // 4, j * squer_size + squer_size // 4, text_size, str(3), (0, 255, 255)))
                    
                elif grid[i][j][0] == 4:
                    numbers.append(Text(i * squer_size + squer_size // 4, j * squer_size + squer_size // 4, text_size, str(4), (0, 255, 0)))
                    
                elif grid[i][j][0] == 5:
                    numbers.append(Text(i * squer_size + squer_size // 4, j * squer_size + squer_size // 4, text_size, str(5), (0, 0, 0)))
                    
                elif grid[i][j][0] == 6:
                    numbers.append(Text(i * squer_size + squer_size // 4, j * squer_size + squer_size // 4, text_size, str(6), (255, 0, 255)))
                    
                elif grid[i][j][0] == 7:
                    numbers.append(Text(i * squer_size + squer_size // 4, j * squer_size + squer_size // 4, text_size, str(7), (255, 255, 255)))
                    
                else:
                    numbers.append(Text(i * squer_size + squer_size // 4, j * squer_size + squer_size // 4, text_size, str(8), (255, 0, 0)))
    
    for i in range(x+1):
        pygame.draw.line(win, (0, 0, 0), (i * squer_size, 0), (i * squer_size, win_size[1]), 3)
        
    for i in range(y+1):
        pygame.draw.line(win, (0, 0, 0), (0, i * squer_size), (win_size[1], i * squer_size), 3)
    
    for i in range(len(numbers)):
        numbers[i].draw(win)
    
    pygame.display.update()
    
def game(win, grid, x, y, win_size):
    boxes_completed = 0
    squer_size = win_size[0] // x
    run = True
    
    while run:
        mouse_pos = pygame.mouse.get_pos()
        for event in pygame.event.get():
            if event.type == QUIT:
                run = False
                pygame.quit()
                quit()
            if event.type == MOUSEBUTTONDOWN:
                try:
                    if event.button == 1 and not grid[mouse_pos[0] // squer_size][mouse_pos[1] // squer_size][2] == True:
                        grid[mouse_pos[0] // squer_size][mouse_pos[1] // squer_size][1] = True
                        if grid[mouse_pos[0] // squer_size][mouse_pos[1] // squer_size][0] == "mine":
                            run = False
                            you_lose(win)
                    elif event.button == 3:
                        if not grid[mouse_pos[0] // squer_size][mouse_pos[1] // squer_size][2] == True:
                            grid[mouse_pos[0] // squer_size][mouse_pos[1] // squer_size][2] = True
                        else:
                            grid[mouse_pos[0] // squer_size][mouse_pos[1] // squer_size][2] = False
                except Exception:
                    pass
        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if grid[i][j][0] == 0 and grid[i][j][1] == True:
                    if not i-1 < 0 and not j-1 < 0:
                        grid[i-1][j-1][1] = True
                    if not i-1 < 0:
                        grid[i-1][j][1] = True
                    if not i-1 < 0 and not j+1 >= x:    
                        grid[i-1][j+1][1] = True
                    if not j-1 < 0:
                        grid[i][j-1][1] = True
                    if not j+1 >= x:
                        grid[i][j+1][1] = True
                    if not i+1 >= y and not j-1 < 0 :
                        grid[i+1][j-1][1] = True
                    if not i+1 >= y:
                        grid[i+1][j][1] = True
                    if not j+1 >= x and not i+1 >= y:
                        grid[i+1][j+1][1] = True
                        
        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if grid[i][j][1] == True:
                    boxes_completed += 1
                    
                elif grid[i][j][1] == False and grid[i][j][0] == "mine":
                    boxes_completed += 1
                      
        if boxes_completed == x * y:
            you_win(win)
            run = False
        boxes_completed = 0
        
        redraw_game(grid, x, y, win_size, squer_size)

def you_lose(win):
    clock = pygame.time.Clock()
    you_lose_text = Text(300, 350, 100, "you lose", (255, 100, 100))
    for i in range(5):
        you_lose_text.draw(win)
        pygame.display.update()
        
    clock.tick(1)
    
def you_win(win):
    clock = pygame.time.Clock()
    you_win_text = Text(300, 350, 100, "you win", (100, 255, 100))
    for i in range(5):
        you_win_text.draw(win)
        pygame.display.update()
        
    clock.tick(1)

def main(win, win_size):
    while True:
        lobby(win)
        
        proprties = dificulty(win)  
        
        grid = make_grid(proprties[0], proprties[1])
        chcose_mines(grid, proprties[2], proprties[0], proprties[1])
        update_grid(grid, proprties[0], proprties[1])
        #print(grid)
        game(win, grid, proprties[0], proprties[1], win_size)
    
main(win, win_size)