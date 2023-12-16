from typing import Any

import pygame
from pygame.surface import SurfaceType, Surface

from system import TILE_WIDTH, TILE_HEIGHT, WALL_TILE

all_sprites = pygame.sprite.Group()
tiles_group = pygame.sprite.Group()
player_group = pygame.sprite.Group()


class Tile(pygame.sprite.Sprite):
    def __init__(self, image: Surface | SurfaceType, pos: tuple[int, int]):
        super().__init__(tiles_group, all_sprites)
        self.image = image
        self.rect = self.image.get_rect().move(
            TILE_WIDTH * pos[0], TILE_HEIGHT * pos[1])


class Player(pygame.sprite.Sprite):
    def __init__(self, game_level: list[str], pos: tuple[int, int],
                 image: Surface | SurfaceType):

        super().__init__(player_group, all_sprites)

        self.game_field = game_level
        self.tile_x, self.tile_y = pos
        self.image = image

        self.rect = self.image.get_rect().move(
            TILE_WIDTH * pos[0] + 15, TILE_HEIGHT * pos[1] + 5)

    def move(self, tile_x, tile_y):
        self.rect = self.rect.move(
            TILE_WIDTH * (tile_x - self.tile_x),
            TILE_HEIGHT * (tile_y - self.tile_y)
        )
        self.tile_x, self.tile_y = tile_x, tile_y

    def update(self, *args: Any, **kwargs: Any) -> None:
        new_tile_x, new_tile_y = self.tile_x, self.tile_y
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            new_tile_x -= 1
        elif keys[pygame.K_RIGHT]:
            new_tile_x += 1
        elif keys[pygame.K_DOWN]:
            new_tile_y += 1
        elif keys[pygame.K_UP]:
            new_tile_y -= 1

        if self.is_empty_tile(new_tile_x, new_tile_y):
            self.move(new_tile_x, new_tile_y)

    def is_empty_tile(self, tile_x, tile_y):
        return self.game_field[tile_y][tile_x] != WALL_TILE
