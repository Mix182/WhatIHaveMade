def make_data(colors, run=True):
    data = []

    if not run:
        return data

    binary = []

    insert = []
    for i in range(len(colors)):
        insert.append(0)

    for i in range(2 ** len(colors)):
        binary.append([])
        for j in insert:
            binary[i].append(j)
        
        insert[0] += 1
        try:
            for j in range(len(insert)):
                if insert[j] == 2:
                    insert[j+1] += 1
                    insert[j] = 0
        except Exception:
            pass

    l = (2 ** len(colors)) ** 0.5

    for i in range(len(binary)):
        x = round(i % l)
        y = i // l
        for j in range(len(binary[i])):
            if binary[i][j] == 1:
                data.append({"x": x, "y": y, "c": colors[j]})

    return data

def main(grid, win, clock, colors):
    def draw(grid, win, bg, clock, mp, clr):
        win.fill(bg)

        grid.draw()

        pygame.draw.rect(win, clr, (mp[0] - grid.sw / 6, mp[1] - grid.sh / 6, grid.sw / 3, grid.sh / 3))

        pygame.display.update()

        clock.tick(60)

    color = 0

    run = True

    mbd = False
    ctrl = False

    bgc = (255, 255, 255)

    while run:
        for event in pygame.event.get():
            if event.type == QUIT:
                run = False
                pygame.quit()
                quit()
            if event.type == MOUSEBUTTONDOWN:
                if not event.button > 3:
                    mbd = event.button

                elif event.button == 4:
                    if ctrl:
                        grid.update(win, grid.scx - 1, grid.scy - 1)
                    else:
                        color += 1
                        if color >= len(colors):
                            color = 0

                        grid.c = colors[color]

                        time.sleep(0.25)

                elif event.button == 5:
                    if ctrl:
                        grid.update(win, grid.scx + 1, grid.scy + 1)
                    else:
                        color -= 1
                        if color <= 0:
                            color = len(colors) - 1

                        grid.c = colors[color]

                        time.sleep(0.25)
            
            if event.type == MOUSEBUTTONUP:
                mbd = False

            if event.type == VIDEORESIZE:
                win_size = [event.w, event.h]
                win = pygame.display.set_mode(win_size, pygame.RESIZABLE)
                grid.update(win, grid.scx, grid.scy)

            if event.type == KEYDOWN:
                if event.key == K_LCTRL:
                    ctrl = True
                
                elif event.key == K_e:
                    grid.clear()
                    
            if event.type == KEYUP:
                if event.key == K_LCTRL:
                    ctrl = False

        
        mouse_pos = pygame.mouse.get_pos()
        

        if mbd == 1:
            grid.place(mouse_pos)

        elif mbd == 3:
            grid.destroy(mouse_pos)

        draw(grid, win, bgc, clock, mouse_pos, colors[color])


if __name__ == "__main__":
    import pygame
    from pygame.locals import *

    import time

    from grid2 import Grid

    win_size = [1000, 1000]

    pygame.init()
    win = pygame.display.set_mode(win_size, pygame.RESIZABLE)

    pygame.display.set_caption("Outline test")

    
    colors = [(0, 0, 0), (255, 0, 0), (0, 255, 0), (0, 0, 255), (255, 255, 0), (255, 0, 255), (0, 255, 255), (255, 255, 255)]
    #colors = [(0, 0, 0), (255, 0, 0), (0, 255, 0), (0, 0, 255)]

    grid = Grid(win, 16, 16, data=make_data(colors, False), alpha=73)

    clock = pygame.time.Clock()

    main(grid, win, clock, colors)