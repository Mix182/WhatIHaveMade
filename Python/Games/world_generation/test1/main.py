def main(win):
    clock = pygame.time.Clock()

    grid = Map(win, grid_size, colors)

    run = True

    mbd = False
    kbd = False

    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                pygame.quit()
                quit()
                
            if event.type == pygame.MOUSEBUTTONDOWN:
                mbd = event.button

            if event.type == pygame.MOUSEBUTTONUP:
                mbd = False

            if event.type == pygame.KEYDOWN:
                kbd = event.key

            if event.type == pygame.KEYUP:
                kbd = False

        update(mbd, kbd, grid)
        
        draw(win, clock, [grid])
        
        

def draw(win, clock, stuff=[], fps=30, BG_color=(255, 255, 255)):
    win.fill(BG_color)
    
    for i in stuff:
        i.draw()
        
    pygame.display.update()
    clock.tick(fps)

def update(mbd, kbd, grid):
    if kbd == pygame.K_r:
        grid.change_selected("r")

    elif kbd == pygame.K_w:
        grid.change_selected("^")

    elif kbd == pygame.K_s:
        grid.change_selected("v")

    elif kbd == pygame.K_a:
        grid.change_selected("<")

    elif kbd == pygame.K_d:
        grid.change_selected(">")

    if mbd == 9:
        grid.change_selected("vv")

    elif mbd == 8:
        grid.change_selected("^^")


if __name__ == "__main__":
    from classes import *

    import pygame

    from noise import pnoise2, snoise2


    from changables import win_size, grid_size, colors

    win = pygame.display.set_mode(win_size)

    pygame.display.set_caption("World Generation")

    main(win)