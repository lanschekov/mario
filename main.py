import sys

import pygame

from sprite import Tile, Player
from sprite import tiles_group, player_group
from system import EMPTY_TILE, WALL_TILE, PLAYER_TILE, MAP_FILE
from system import EMPTY_TILE_IMAGE, WALL_TILE_IMAGE, PLAYER_IMAGE
from system import SCREEN, WIDTH, HEIGHT, FPS
from system import load_image, load_level, LEVEL


def terminate():
    pygame.quit()
    sys.exit()


def start_screen():
    intro_text = ['ЗАСТВАКА', 'Правила игры',
                  'Если в правилах несколько строк,',
                  'приходится выводить их построчно']
    fon = pygame.transform.scale(load_image('fon.jpg'), (WIDTH, HEIGHT))
    SCREEN.blit(fon, (0, 0))

    font = pygame.font.Font(None, 30)
    text_coord = 50
    for line in intro_text:
        string_rendered = font.render(line, True, pygame.Color('black'))
        intro_rect = string_rendered.get_rect()
        text_coord += 10
        intro_rect.top = text_coord
        intro_rect.x = 10
        text_coord += intro_rect.height
        SCREEN.blit(string_rendered, intro_rect)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                terminate()
            elif event.type == pygame.KEYDOWN or \
                event.type == pygame.MOUSEBUTTONDOWN:
                return  # Start the game
        pygame.display.flip()
        clock.tick(FPS)


def generate_level(level):
    new_player = x = y = None
    for y in range(len(level)):
        for x in range(len(level[y])):
            if level[y][x] == EMPTY_TILE:
                Tile(EMPTY_TILE_IMAGE, (x, y))
            elif level[y][x] == WALL_TILE:
                Tile(WALL_TILE_IMAGE, (x, y))
            elif level[y][x] == PLAYER_TILE:
                Tile(EMPTY_TILE_IMAGE, (x, y))
                new_player = Player(LEVEL, (x, y), PLAYER_IMAGE)
    return new_player, x, y


if __name__ == '__main__':
    clock = pygame.time.Clock()
    start_screen()

    player, level_x, level_y = generate_level(load_level(MAP_FILE))

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                terminate()

        SCREEN.fill((0, 0, 0))

        tiles_group.draw(SCREEN)
        tiles_group.update()

        player_group.draw(SCREEN)
        player_group.update()

        pygame.display.flip()
        clock.tick(FPS)
