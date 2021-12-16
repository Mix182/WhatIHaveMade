import pygame, os

def dict(dir, textures, file_types=["png", "jpg", "jpeg"]):
    for fod in os.scandir(dir):
        if fod.is_dir():
            textures[fod.name] = {}
            dict(fod.path, textures[fod.name])

        elif fod.is_file():
            for type in file_types:
                if fod.path.endswith(type):
                    textures[fod.name.split(".")[0]] = pygame.image.load(fod.path)
                else:
                    pass
    return textures

textures = dict("./assets", {})