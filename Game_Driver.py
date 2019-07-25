import pygame
import pygame.math
import os
import importlib
import functions, Pokemon
import tcp_client
from pygame.locals import *


SCREENSIZE_X = 1000
SCREENSIZE_Y = 618
CONVERSION_FACTOR = 50
BACKPACK_SIZE = 6
# these coordinates are bounding points
# Giant search bar for screen 3
# screen 3 consists of a single search button
# jumps to external terminal
# name becomes input 
# search for name within pokemon pool
# 
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
    #os.chdir(r'C:\Users\jeffr\OneDrive\Desktop\VS2020\BattleSimulation\Pokemon-Battle-Simulation')
    pokemon_lst = functions.poke_lst()
    choice_lst = []
    screen = pygame.display.set_mode((SCREENSIZE_X, SCREENSIZE_Y))
    pygame.display.set_caption('home screen')
    #booleans for disabling screen functions
    active_Screen = True
    active_Screen2 = False
    active_Screen3 = False
    active_Screen4 = False
    #booleans for button functions
    active_start = False
    active_help = False
    active_server = False
    active_client = False
    active_enter = False
    active_search = False
    active_startgame = False
    finished_choice = False

    screen.fill((255, 255, 255))
    user_choice = ''
    running = True
    display_Homescreen(screen)
    #start_button = button('C:\\Users\\jeffr\\OneDrive\\Desktop\\VS2020\\BattleSimulation\\Pokemon-Battle-Simulation\\asset\\image\\start.png', 700, 490, 900, 615)
    start_button = button('asset\\image\\start.png', 700, 490, 900, 615)
    start_button.show_button(screen)
    help_button = button('asset\\image\\help.png', 200, 500, 400, 600)
    help_button.show_button(screen)
    lst = start_button.coordinates()
    alst = help_button.coordinates()
    server_button = button('asset\\image\\server.png', 600, 50, 700, 300)
    #server_button.show_button(screen2)
    client_button = button('asset\\image\\client.png', 750, 50, 900, 300)
    #client_button.show_button(screen2)
    #display_Image(screen2, 'Pokemon-Battle-Simulation\\asset\\image\\selection.png', 200, 50, 550, 150)
    enter_button = button('asset\\image\\enter.jpg', 800, 525, 950, 600)
    slst = server_button.coordinates()
    clst = client_button.coordinates()
    elst = enter_button.coordinates()
    search_button = button('asset\\image\\Magnify.png', SCREENSIZE_X//2 - 200, SCREENSIZE_Y//2 - 150, SCREENSIZE_X//2 + 200, SCREENSIZE_Y//2 + 150)
    srchLst = search_button.coordinates()
    startgame_button = button('asset\\image\\play.jpg', 850, 490, 1000, 615)
    sglst = startgame_button.coordinates()
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
            mts(screen, font, "Please choose your character", (0,0,0), slst[0] - 400, slst[1])
            active_start = False
            active_Screen = False
        if active_server == True:
            display_Image(screen, 'asset\\image\\art.jpg',slst[0] - 10, slst[3] + 10, slst[2] + 10, slst[3] + 50)
            active_server = False
            user_ip = input(screen, font)
            user_port = input(screen, font)
            client = tcp_client.client(user_ip, int(user_port))
            
        elif active_client == True:
            display_Image(screen, 'asset\\image\\art.jpg',clst[0] - 10, clst[3] + 10, clst[2] - 10, clst[3] + 50)
            active_client = False
        if active_enter == True:
            display_Background(screen)
            search_button.show_button(screen)
            mts(screen, font, "Search For a Pokemon to Make Your Deck", (0,0,0), srchLst[0] - 20, srchLst[1] - 50)
            startgame_button.show_button(screen)
            active_Screen2 == False
        if active_search == True:
            mts(screen, font, "BACKPACK", (0, 0, 255), 800, 50)
            for x in range(BACKPACK_SIZE):
                user_choice = input(screen, font)
                while(not check_lst(user_choice, pokemon_lst)):
                    print("Please enter a valid pokemon")
                    user_choice = input(screen, font)
                if(check_lst(user_choice, pokemon_lst)):
                    choice_lst.append(Pokemon.Pokemon(user_choice))
                    mts(screen, font, user_choice, (0, 0, 0), 800, (x + 2) * CONVERSION_FACTOR)
            finished_choice = True
        if active_startgame:
            pass

                
            
            
                
                    
            
             
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
                    active_Screen3 = True
                if check_Bounds(srchLst) and active_Screen3:
                    active_search = True
                if check_Bounds(sglst) and active_Screen3 and finished_choice:
                    active_startgame = True
                    active_Screen4 = True
                
                    
                
                
        pygame.display.update()

def check_lst(name, lst):
    return name in lst
def input(screen, font, name = ''):
    while True:
        for evt in pygame.event.get():
            if evt.type == KEYDOWN:
                if evt.unicode.isalpha():
                    name += evt.unicode
                elif evt.key == K_BACKSPACE:
                    name = name[:-1]
                elif evt.key == K_RETURN:
                    return name
                    name = ""
            elif evt.type == QUIT:
                break
        display_Image(screen, 'asset\\image\\textbox.png', 250, 518, 800, 618)
        block = font.render(name, True, (255, 255, 255))
        rect = block.get_rect()
        rect.center = (550, 568)
        screen.blit(block, rect)
        pygame.display.flip()
    
    

def get_Pokemon(screen): 
    user_input = input("Please enter your wanted pokemon")
    return user_input

def mts(screen, font, text, textcolor, x, y):
    text = font.render(text, True, textcolor)
    screen.blit(text, [x, y])
    #pygame.display.update()

def display_Image(screen, file_abspath, x1, y1, x2, y2 ):
    image = pygame.transform.scale(pygame.image.load(file_abspath), (abs(x2 - x1), abs(y2 - y1)))
    screen.blit(image, (x1, y1))
    #pygame.display.update()

def display_Homescreen(screen):
    homescreen = pygame.transform.scale(pygame.image.load('asset\\image\\colorscreen.jpg'), (SCREENSIZE_X, SCREENSIZE_Y))
    screen.blit(homescreen, (0, 0))
    #pygame.display.update()

def check_Bounds(lst):
    if pygame.mouse.get_pos()[0] > lst[0] and pygame.mouse.get_pos()[0] < lst[2] and pygame.mouse.get_pos()[1] > lst[1] and pygame.mouse.get_pos()[1] < lst[3]:
        return True
    return False

def display_Background(screen):
    background = pygame.transform.scale(pygame.image.load('asset\\image\\white.png'), (SCREENSIZE_X, SCREENSIZE_Y))
    screen.blit(background, (0, 0))

    #pygame.display.update()


main()
