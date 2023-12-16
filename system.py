import os
import sys

import pygame

FPS = 10
SIZE = WIDTH, HEIGHT = 550, 550
TILE_WIDTH = TILE_HEIGHT = 50

pygame.init()
SCREEN = pygame.display.set_mode(SIZE)


def load_image(name, color_key=None):
    fullname = os.path.join('data', name)
    # если файл не существует, то выходим
    if not os.path.isfile(fullname):
        print(f"Файл с изображением '{fullname}' не найден")
        sys.exit()
    image = pygame.image.load(fullname)

    if color_key is not None:
        image = image.convert()
        if color_key == -1:
            color_key = image.get_at((0, 0))
        image.set_colorkey(color_key)
    else:
        image = image.convert_alpha()
    return image


EMPTY_TILE_IMAGE = load_image('grass.png')
WALL_TILE_IMAGE = load_image('box.png')
PLAYER_IMAGE = load_image('mario.png')

EMPTY_TILE = '.'
WALL_TILE = '#'
PLAYER_TILE = '@'
MAP_FILE = 'map.txt'


def load_level(filename):
    filename = "data/" + filename
    # читаем уровень, убирая символы перевода строки
    with open(filename, 'r') as mapFile:
        level_map = [line.strip() for line in mapFile]

    # и подсчитываем максимальную длину
    max_width = max(map(len, level_map))

    # дополняем каждую строку пустыми клетками
    return list(map(lambda x: x.ljust(max_width, EMPTY_TILE), level_map))


LEVEL = load_level(MAP_FILE)
