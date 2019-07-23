import pygame
from pygame.locals import *

SCREENSIZE_X = 1000
SCREENSIZE_Y = 618

def main():
    screen = pygame.display.set_mode((SCREENSIZE_X, SCREENSIZE_Y))
    pygame.display.set_caption('Battle Simulation')
    screen.fill((255, 255, 255))
    background = pygame.transform.scale(pygame.image.load('C:\\Users\\jeffr\\OneDrive\\Desktop\\VS2020\\BattleSimulation\\Pokemon-Battle-Simulation\\asset\\image\\background.png'), (SCREENSIZE_X, SCREENSIZE_Y))
   
    screen.blit(background, (0, 0))
    pygame.display.update()

    running = True
    while running:
	    for event in pygame.event.get():
		    if event.type == pygame.QUIT:
			    running = False

main()