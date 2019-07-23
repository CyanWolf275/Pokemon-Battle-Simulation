import pygame
from pygame.locals import *

SCREENSIZE_X = 1000
SCREENSIZE_Y = 618

def main():
    screen = pygame.display.set_mode((1024, 768))
    pygame.display.set_caption('Battle Simulation')
    screen.fill((255, 255, 255))
    background = pygame.image.load("background.png")
    screen.blit(background, (250, 250))
    pygame.display.update()

main()