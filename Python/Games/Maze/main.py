from classes import *

from maps import maps

import pygame
from pygame.locals import KEYDOWN, KEYUP, QUIT, K_w, K_s, K_a, K_d, K_e, K_q

pygame.font.init()

win_size = [1000, 1000]
win = pygame.display.set_mode(win_size)

game_name = "Maze"
pygame.display.set_caption(game_name)

def redraw(win, bg, clock, stuff=[]):
    try:
        win.fill(bg)
    except Exception:
        win.blit(pygame.transform.scale(bg, (win.get_width(), win.get_height())), (0, 0))

    for i in stuff:
        i.draw()

    clock.tick(30)

    pygame.display.update()

def main(win):
    clock = pygame.time.Clock()

    lvl = 0

    grid = Map(win, maps[lvl])
    player = Player(win, grid)

    movment = [0, 0, 0, 0]

    run = True
    while run:
        for event in pygame.event.get():
            if event.type == QUIT:
                run = False
                pygame.quit()
                quit()

            elif event.type == KEYDOWN:
                if event.key == K_w: movment[0] = 1
                elif event.key == K_s: movment[1] = 1
                elif event.key == K_a: movment[2] = 1
                elif event.key == K_d: movment[3] = 1
                elif event.key == K_e: player.up()
                elif event.key == K_q: player.down()

            elif event.type == KEYUP:
                if event.key == K_w: movment[0] = 0
                elif event.key == K_s: movment[1] = 0
                elif event.key == K_a: movment[2] = 0
                elif event.key == K_d: movment[3] = 0

        if player.update(movment):
            if lvl + 1 >= len(maps): lvl = 0
            else: lvl += 1
            grid = Map(win, maps[lvl])
            player = Player(win, grid)
        
        redraw(win, (0, 0, 0), clock, [grid, player])


if __name__ == "__main__":
    main(win)