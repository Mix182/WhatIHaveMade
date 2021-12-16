import pygame, os

def dict(dir, textures):
    for fod in os.scandir(dir):
        if fod.is_dir():
            textures[fod.name] = {}
            dict(fod.path, textures[fod.name])

        elif fod.is_file():
            if not fod.path.endswith(".png"):
                pass
            else:
                textures[fod.name.split(".")[0]] = pygame.image.load(fod.path)

    return textures

textures = dict("/home/pi/Desktop/Programování/Python/Projekty/My games/miner/assets", {})