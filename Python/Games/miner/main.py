def main(win, clock):
    win_size = [win.get_width(), win.get_height()]

    scene = starting_scene

    mbd = False
    kbd = False

    if win_size[0] > win_size[1]:
        w = win_size[1] // cos

    else:
        w = win_size[0] // cos

    player = Player(win, textures["Player"], w, w)
    grid = Map(win, player, cos, textures)

    player.grid = grid

    run = True

    while run:
        for event in pygame.event.get():
            if event.type == QUIT:
                run = False
                pygame.quit()
                quit()

            if event.type == MOUSEBUTTONDOWN:
                mbd = event.button
                
            if event.type == MOUSEBUTTONUP:
                mbd = False

            if event.type == VIDEORESIZE:
                win_size = [event.w, event.h]
                win = pygame.display.set_mode(win_size, pygame.RESIZABLE)

            if event.type == KEYDOWN:
                kbd = event.key
                    
            if event.type == KEYUP:
                kbd = False

        mouse_pos = pygame.mouse.get_pos()

        update(kbd, mbd, grid)

        draw(win, (0, 122, 255), clock, [player])

def update(kbd, mbd, grid):
    grid.player.move(kbd)

def draw(win, BG_color, clock, stuff=[]):
    win.fill(BG_color)
    
    for i in stuff:
        i.draw()
        
    pygame.display.update()
    clock.tick(60)

if __name__ == "__main__":
    import pygame
    from pygame.locals import *

    from changables import *

    from assets import textures
    from classes import *

    win = pygame.display.set_mode(win_size)

    clock = pygame.time.Clock()

    main(win, clock)
