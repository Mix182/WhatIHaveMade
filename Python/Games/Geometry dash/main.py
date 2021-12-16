import pygame
from pygame.locals import *
from classes import *

def redraw(win, BG_color, draw_stuf = []):
    clock = pygame.time.Clock()
    clock.tick(60)
    
    win.fill(BG_color)
    
    for i in range(len(draw_stuf)):
        draw_stuf[i].draw()
        
    pygame.display.update()

def lobby(win):
    BG_color = (0, 0, 0)
    
    start_button = Button(300, 350, 200, 100, (0, 255, 0), "Play", win)
    quit_button = Button(300, 500, 200, 100, (255, 0, 0), "Quit", win)
    
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
                    game(win)
                    
                if quit_button.is_touching(mouse_pos):
                    run = False
                    pygame.quit()
                    quit()
        
        redraw(win, BG_image, [start_button, quit_button])
        
def game(win):
    pass
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    

