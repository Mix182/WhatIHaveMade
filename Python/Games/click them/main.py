import pygame
from pygame.locals import *
from classes import *

win = pygame.display.set_mode((800, 800))
pygame.display.set_caption("Click them")

def redraw(win, block, score):
    win.fill((0, 0, 0))
    
    block.draw_all()
    score.draw()
    
    pygame.display.update()    

def main(win):
    mouse_button_down = False
    
    score = Text(10, 10, 60, "Points: " + str(Block.score.score), win, (255, 255, 255))
    
    run = True
    while run:
        for event in pygame.event.get():
            if event.type == QUIT:
                run = False
                pygame.quit()
                quit()
                
            if event.type == MOUSEBUTTONDOWN:
                mouse_button_down = True
                
            else:
                mouse_button_down = False
                
        mouse_pos = pygame.mouse.get_pos()
        
        Block.new(win)
        Block.update_all(mouse_pos, mouse_button_down)
        score.change_text("Points: " + str(Block.score.score))
        
        redraw(win, Block, score)
        
main(win)