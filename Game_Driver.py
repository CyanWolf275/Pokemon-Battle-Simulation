import pygame
import pygame.math
import os
import pokemon

from pygame.locals import *

SCREENSIZE_X = 1000
SCREENSIZE_Y = 618
CONVERSION_FACTOR = 50
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
    #print(os.getcwd())
    screen = pygame.display.set_mode((SCREENSIZE_X, SCREENSIZE_Y))
    pygame.display.set_caption('home screen')
    #booleans for disabling button functions
    active_Screen = True
    active_Screen2 = False
    #booleans for button functions
    active_start = False
    active_help = False
    active_server = False
    active_client = False
    active_enter = False
    screen.fill((255, 255, 255))
    lst_pokemon = []
    running = True
    display_Homescreen(screen)
    #start_button = button('C:\\Users\\jeffr\\OneDrive\\Desktop\\VS2020\\BattleSimulation\\Pokemon-Battle-Simulation\\asset\\image\\start.png', 700, 490, 900, 615)
    start_button = button('Pokemon-Battle-Simulation\\asset\\image\\start.png', 700, 490, 900, 615)
    start_button.show_button(screen)
    help_button = button('Pokemon-Battle-Simulation\\asset\\image\\help.png', 200, 500, 400, 600)
    help_button.show_button(screen)
    lst = start_button.coordinates()
    alst = help_button.coordinates()
    server_button = button('Pokemon-Battle-Simulation\\asset\\image\\server.png', 600, 50, 700, 300)
    #server_button.show_button(screen2)
    client_button = button('Pokemon-Battle-Simulation\\asset\\image\\client.png', 750, 50, 900, 300)
    #client_button.show_button(screen2)
    #display_Image(screen2, 'Pokemon-Battle-Simulation\\asset\\image\\selection.png', 200, 50, 550, 150)
    enter_button = button('Pokemon-Battle-Simulation\\asset\\image\\enter.jpg', 800, 525, 950, 600)
    slst = server_button.coordinates()
    clst = client_button.coordinates()
    elst = enter_button.coordinates()
    while running:

        #Creation of homescreen and a couple buttons
        #one screen, button booleans
        if active_start == True:
            #screen = pygame.display.set_mode((SCREENSIZE_X, SCREENSIZE_Y))
            #pygame.display.set_caption('index screen')
            display_Background(screen)
            server_button.show_button(screen)
            client_button.show_button(screen)
            enter_button.show_button(screen)
            pygame.font.init()
            font = pygame.font.SysFont("arial", 24)
            mts(screen, font, "Ash", (0, 0, 0), 625, 320)
            mts(screen, font, "Serena", (0, 0, 0), 765, 320)
            active_start = False
            active_Screen = False
        if active_server == True:
            display_Image(screen, 'Pokemon-Battle-Simulation\\asset\\image\\art.jpg',slst[0] - 10, slst[3] + 10, slst[2] + 10, slst[3] + 50)
            active_server = False
        elif active_client == True:
            display_Image(screen, 'Pokemon-Battle-Simulation\\asset\\image\\art.jpg',clst[0] - 10, clst[3] + 10, clst[2] - 10, clst[3] + 50)
        if active_enter == True:
            display_Background(screen)
            

            
             
        for event in pygame.event.get():
           
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                if check_Bounds(lst) and active_Screen:
                    
                    active_start = True
                    active_Screen2 = True
                if(check_Bounds(slst) and active_Screen2):
                    active_server = True
                    #display_Line(screen2, (255,0,0), slst[0] - 10, slst[3] + 10, slst[2] + 10, slst[3] + 50)
                elif(check_Bounds(clst) and active_Screen2):
                    active_client = True
                elif(check_Bounds(elst) and active_Screen2):
                    active_enter = True
                
        pygame.display.update()

def mts(screen, font, text, textcolor, x, y):
    text = font.render(text, True, textcolor)
    screen.blit(text, [x, y])
    #pygame.display.update()

def display_Image(screen, file_abspath, x1, y1, x2, y2 ):
    image = pygame.transform.scale(pygame.image.load(file_abspath), (abs(x2 - x1), abs(y2 - y1)))
    screen.blit(image, (x1, y1))
    #pygame.display.update()

def display_Homescreen(screen):
    homescreen = pygame.transform.scale(pygame.image.load('Pokemon-Battle-Simulation\\asset\\image\\colorscreen.jpg'), (SCREENSIZE_X, SCREENSIZE_Y))
    screen.blit(homescreen, (0, 0))
    #pygame.display.update()

def check_Bounds(lst):
    if pygame.mouse.get_pos()[0] > lst[0] and pygame.mouse.get_pos()[0] < lst[2] and pygame.mouse.get_pos()[1] > lst[1] and pygame.mouse.get_pos()[1] < lst[3]:
        return True
    return False

def display_Background(screen):
    background = pygame.transform.scale(pygame.image.load('Pokemon-Battle-Simulation\\asset\\image\\white.png'), (SCREENSIZE_X, SCREENSIZE_Y))
    screen.blit(background, (0, 0))

    #pygame.display.update()


main()
