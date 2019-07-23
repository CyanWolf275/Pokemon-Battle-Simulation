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
        pygame.display.update()
    '''
    def interaction(self, screen):
        if(pygame.mouse.get_pressed()[0]):
            if(pygame.mouse.get_pos()[0] < self.x2 and pygame.mouse.get_pos()[0] > self.x1 and pygame.mouse.get_pos()[1] > self.y1 and pygame.mouse.get_pos()[1] < self.y2):
                return True
        return False
    '''
    def coordinates(self):
        return[self.x1,self.y1,self.x2,self.y2]
    
def main():
    screen = pygame.display.set_mode((SCREENSIZE_X, SCREENSIZE_Y))
    pygame.display.set_caption('home screen')
    screen.fill((255, 255, 255))
    #Creation of homescreen and a couple buttons
    display_Homescreen(screen)
    start_button = button('C:\\Users\\jeffr\\OneDrive\\Desktop\\VS2020\\BattleSimulation\\Pokemon-Battle-Simulation\\asset\\image\\start.png', 700, 490, 900, 615)
    start_button.show_button(screen)
    help_button = button('C:\\Users\\jeffr\\OneDrive\\Desktop\\VS2020\\BattleSimulation\\Pokemon-Battle-Simulation\\asset\\image\\help.png', 200, 500, 400, 600)
    help_button.show_button(screen)
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                lst = start_button.coordinates()
                alst = help_button.coordinates()
                if check_Bounds(lst):
                    screen2 = pygame.display.set_mode((SCREENSIZE_X, SCREENSIZE_Y))
                    pygame.display.set_caption('index screen')
                    display_Background(screen2)
                    server_button = button('C:\\Users\\jeffr\\OneDrive\\Desktop\\VS2020\\BattleSimulation\\Pokemon-Battle-Simulation\\asset\\image\\server.png', 600, 50, 700, 300)
                    server_button.show_button(screen2)
                    client_button = button('C:\\Users\\jeffr\\OneDrive\\Desktop\\VS2020\\BattleSimulation\\Pokemon-Battle-Simulation\\asset\\image\\client.png', 750, 50, 900, 300)
                    client_button.show_button(screen2)
                    display_Image(screen2, 'C:\\Users\\jeffr\\OneDrive\\Desktop\\VS2020\\BattleSimulation\\Pokemon-Battle-Simulation\\asset\\image\\selection.png', 200, 50, 550, 150)
                    slst = server_button.coordinates()
                    clst = client_button.coordinates()
                    #display_Text(screen2, "Have Funn")
                    pygame.font.init()
                    font = pygame.font.Font(None, 60)
                    mts(screen2, font, "hey", (0,0,0), 150, 150)


def mts(screen, font, text, textcolor, x, y):
    text = font.render(text, True, textcolor)
    screen.blit(text, [x, y])
    pygame.display.update

def display_Image(screen, file_abspath, x1, y1, x2, y2 ):
    image = pygame.transform.scale(pygame.image.load(file_abspath), (abs(x2 - x1), abs(y2 - y1)))
    screen.blit(image, (x1, y1))
    pygame.display.update()

def display_Text(screen, text):
    font = pygame.font.Font('Aerial', 32)
    textSurface = font.render(text, True, "black")
    rect = textSurface.get_rect()
    rect.center = (100, 100)
    screen.blit(textSurface, rect)
    pygame.display.update()

def display_Homescreen(screen):
    homescreen = pygame.transform.scale(pygame.image.load('C:\\Users\\jeffr\\OneDrive\\Desktop\\VS2020\\BattleSimulation\\Pokemon-Battle-Simulation\\asset\\image\\colorscreen.jpg'), (SCREENSIZE_X, SCREENSIZE_Y))
    screen.blit(homescreen, (0, 0))
    pygame.display.update()

def check_Bounds(lst):
    if pygame.mouse.get_pos()[0] > lst[0] and pygame.mouse.get_pos()[0] < lst[2] and pygame.mouse.get_pos()[1] > lst[1] and pygame.mouse.get_pos()[1] < lst[3]:
        return True
    return False

def display_Background(screen):
    background = pygame.transform.scale(pygame.image.load('C:\\Users\\jeffr\\OneDrive\\Desktop\\VS2020\\BattleSimulation\\Pokemon-Battle-Simulation\\asset\\image\\white.png'), (SCREENSIZE_X, SCREENSIZE_Y))
    
    screen.blit(background, (0, 0))

    pygame.display.update()
   
main()
