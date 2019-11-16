import pygame


def convert(pos):
    x, y = pos
    screenY = pygame.display.get_surface().get_size()[1]
    return (x, screenY - y)