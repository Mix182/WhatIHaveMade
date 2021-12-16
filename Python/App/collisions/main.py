import pygame

from classes import Wall
from classes import Block

blocks = [Block(700, 400, 10, 1, 50, (200, 200, 200))]
walls = [Wall(700, 100, (255, 255, 255))]

win = pygame.display.set_mode((800, 800))
pygame.display.set_caption("Collisions")

def draw(win, blocks, walls):
    win.fill((0, 0, 0))

    for b in blocks:
        b.draw(win)

    for w in walls:
        w.draw(win)

    pygame.display.update()

def main(win, blocks, walls):

    run = True
    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                pygame.quit()
                quit()

        draw(win, blocks, walls)


if __name__ == "__main__":
    main(win, blocks, walls) 
