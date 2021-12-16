import pygame
from pygame.locals import *
from classes import *

clock = pygame.time.Clock()
win_size = [800, 600]

pygame.init()
win = pygame.display.set_mode(win_size, 0, 32)

pygame.display.set_caption("Points")

def lobby(win, win_size, clock):
    run = True
    Play_button = Button(300, 200, 200, 100, (0, 255, 0), "Play")
    Quit_button = Button(300, 400, 200, 100, (255, 0, 0), "Quit")
    
    while run:
        mouse_pos = pygame.mouse.get_pos()
        
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                quit()
            
            if event.type == MOUSEBUTTONDOWN:
                if Play_button.is_touching(mouse_pos):
                    game(win, clock)
                    
                elif Quit_button.is_touching(mouse_pos):
                    pygame.quit()
                    quit()
        
        redraw_lobby(win, clock, Play_button, Quit_button)
    
def redraw_lobby(win, clock, Play_button, Quit_button):
    win.fill((0, 200, 255))
    
    Play_button.draw(win)
    Quit_button.draw(win)
    
    clock.tick(60)
    pygame.display.update()

def game(win, clock):
    run = True
    points = []
    for i in range(random.randint(50, 100)):
        points.append(Point(win_size))
        
    player1 = Player(100, 100)
    player2 = Player(600, 600)
    
    while run:
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                quit()
                
            if event.type == KEYDOWN:
                if event.key == K_w:
                    player1.moving_up = True
                    
                if event.key == K_s:
                    player1.moving_down = True
                    
                if event.key == K_d:
                    player1.moving_right = True
                    
                if event.key == K_a:
                    player1.moving_left = True
                    
            if event.type == KEYUP:
                if event.key == K_w:
                    player1.moving_up = False
                    
                if event.key == K_s:
                    player1.moving_down = False
                    
                if event.key == K_d:
                    player1.moving_right = False
                    
                if event.key == K_a:
                    player1.moving_left = False
                    
        for i in range(len(points)):
            points[i].is_touching(player1, win_size)
            points[i].is_touching(player2, win_size)
        
        player1.move()
        redraw_game(win, clock, points, player1, player2)
    
def redraw_game(win, clock, points, player1, player2):
    win.fill((255, 255, 255))
    
    for i in range(len(points)):
        points[i].draw(win)
        
    player1.draw(win)
    player1.draw(win)
    
    pygame.display.update()
    clock.tick(60)
    
lobby(win, win_size, clock)