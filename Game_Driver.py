import pygame
import pygame.math
from pygame.locals import *

SCREENSIZE_X = 1000
SCREENSIZE_Y = 618
# these coordinates are bounding points
class button:
    def __init__(self, image, x1, y1, x2, y2):
        self.image = image
        self.x1 = x1
        self.x2 = x2
        self.y1 = y1
        self.y2 = y2
    def show_button(self, screen):
        new_image = pygame.transform.scale(pygame.image.load(self.image), (abs(self.x2 - self.x1), abs(self.y2 - self.y1)))
        screen.blit(new_image, (self.x1, self.y1))
    def interaction(self, screen):
        pass
    
def main():
    screen = pygame.display.set_mode((SCREENSIZE_X, SCREENSIZE_Y))
    pygame.display.set_caption('Battle Simulation')
    screen.fill((255, 255, 255))
    #Creation of homescreen and a couple buttons
    display_Homescreen(screen)
    start_button = button('C:\\Users\\jeffr\\OneDrive\\Desktop\\VS2020\\BattleSimulation\\Pokemon-Battle-Simulation\\asset\\image\\start.png', 700, 490, 900, 615)
    start_button.show_button(screen)
    help_button = button('C:\\Users\\jeffr\\OneDrive\\Desktop\\VS2020\\BattleSimulation\\Pokemon-Battle-Simulation\\asset\\image\\help.png', 200, 500, 400, 600)
    help_button.show_button(screen)
    
    pygame.display.update()
    running = True
    while running:
	    for event in pygame.event.get():
		    if event.type == pygame.QUIT:
			    running = False


def display_Image(screen, file_abspath, x, y, scale_x, scale_y):
    image = pygame.transform.scale(pygame.image.load(file_abspath), (scale_x, scale_y))
    screen.blit(image, (x, y))
def display_Homescreen(screen):
    homescreen = pygame.transform.scale(pygame.image.load('C:\\Users\\jeffr\\OneDrive\\Desktop\\VS2020\\BattleSimulation\\Pokemon-Battle-Simulation\\asset\\image\\colorscreen.jpg'), (SCREENSIZE_X, SCREENSIZE_Y))
    screen.blit(homescreen, (0, 0))

def display_Background(screen):
    background = pygame.transform.scale(pygame.image.load('C:\\Users\\jeffr\\OneDrive\\Desktop\\VS2020\\BattleSimulation\\Pokemon-Battle-Simulation\\asset\\image\\water.png'), (SCREENSIZE_X, SCREENSIZE_Y))
    screen.blit(background, (0, 0))
main()
