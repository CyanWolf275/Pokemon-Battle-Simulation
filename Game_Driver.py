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

class game_Pokemon(pygame.sprite.Sprite):
    def __init__(self, x, y, x2, y2, Pokemon):
        self.locationX = x
        self.locationY = y
        self.locationX2 = x2
        self.locationY2 = y2
        self.image = Pokemon.BackPIc
        self.pokemon = Pokemon
        
    def show_image(self, screen):
        display_Image(screen, self.image, self.locationX, self.locationY, self.locationX2, self.locationY2)
    def show_imageE(self, screen):
        display_Image(screen, self.pokemon.FrontPic, self.locationX, self.locationY, self.locationX2, self.locationY2)
    def show_status(self, screen, font):
        draw_box(screen, font, 0 , 0, self.locationX2 + 100, self.locationY2 - 400, self.pokemon.name, self.pokemon.level, self.pokemon.HP, self.pokemon.totalHP)

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
    
    def show_text(self, screen, font):
        new_text = self.image
        text = font.render(self.image, True, [0,0,0])
        screen.blit(text, [(self.x1 + self.x2)//2, (self.y1 + self.y2)//2])
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
    #user_IP = 'jdakdaka'
    #user_Port = 12345678
    #client = tcp_client.client(user_IP, user_Port)
    #client.connect()
    pokemon_lst = functions.poke_lst()
    choice_lst = []
    screen = pygame.display.set_mode((SCREENSIZE_X, SCREENSIZE_Y))
    pygame.display.set_caption('home screen')
    #booleans for disabling screen functions
    active_Screen = True
    active_Screen2 = False
    active_Screen3 = False
    active_Screen4 = False
    active_forloop = True
    #booleans for button functions
    active_start = False
    active_help = False
    active_server = False
    active_client = False
    active_enter = False
    active_search = False
    active_startgame = False
    finished_choice = False
    active_ability1 = False
    active_ability2 = False
    active_ability3 = False
    active_ability4 = False

    screen.fill((255, 255, 255))
    pygame.font.init()
    font = pygame.font.SysFont("arial", 24)
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
    display_Image(screen, 'asset\\image\\Pokemon\\Pikachu.png', 0, 100, 400, 500)
    display_Image(screen, 'asset\\image\\Pokemon\\Charmander.png', 600, 100, 1000, 500)
    
    while running:

        #Creation of homescreen and a couple buttons
        #one screen, button booleans
        if active_start == True:
            #screen = pygame.display.set_mode((SCREENSIZE_X, SCREENSIZE_Y))
            #pygame.display.set_caption('index screen')
            display_Background(screen, 'asset\\image\\white.png')
            server_button.show_button(screen)
            client_button.show_button(screen)
            enter_button.show_button(screen)
           
            mts(screen, font, "Ash", (0, 0, 0), 625, 320)
            mts(screen, font, "Serena", (0, 0, 0), 765, 320)
            mts(screen, font, "Please choose your character", (0,0,0), slst[0] - 400, slst[1])
            active_start = False
            active_Screen = False
        if active_server == True:
            display_Image(screen, 'asset\\image\\art.jpg',slst[0] - 10, slst[3] + 10, slst[2] + 10, slst[3] + 50)
            active_server = False
        elif active_client == True:
            display_Image(screen, 'asset\\image\\art.jpg',clst[0] - 10, clst[3] + 10, clst[2] - 10, clst[3] + 50)
            active_client = False
        if active_enter == True:
            display_Background(screen, 'asset\\image\\white.png')
            search_button.show_button(screen)
            mts(screen, font, "Search For a Pokemon to Make Your Deck", (0,0,0), srchLst[0] - 20, srchLst[1] - 50)
            startgame_button.show_button(screen)
            active_Screen2 == False
        if active_search == True:
            count = 0
            mts(screen, font, "BACKPACK", (0, 0, 255), 800, 50)
            if active_forloop:
                for x in range(BACKPACK_SIZE):
                    user_choice = input1(screen, font)
                    while(not check_lst(user_choice, pokemon_lst)):
                        print("Please enter a valid pokemon")
                        user_choice = input1(screen, font)
                
                    choice_lst.append(Pokemon.Pokemon(user_choice))
                    mts(screen, font, user_choice, (0, 0, 0), 800, (x + 2) * CONVERSION_FACTOR)
                    if(len(choice_lst) == BACKPACK_SIZE):
                        finished_choice = True
                        active_forloop = False

        if finished_choice == True:
        
            active_Screen3 = False
            active_search = False
            active_enter = False
            #screen.fill(255,255,255)
            #mts(screen, font, "Waiting for server to respond", (0,0,0), SCREENSIZE_X//2, 100)
            #client.press_start()
                
            display_Background(screen, 'asset\\image\\background.png')
            current_Pokemon = game_Pokemon(100,200, 300, 500, choice_lst[0])
            enemy_Pokemon = game_Pokemon(700, 0, 900, 200, choice_lst = [])
            current_Pokemon.show_image(screen)
            current_Pokemon.show_status(screen, font)
            ability1 = button(current_Pokemon.pokemon.move_lst[0].name, 20, 440, 120, 450)
            ability2 = button(current_Pokemon.pokemon.move_lst[1].name, 20, 480, 120, 490)
            ability3 = button(current_Pokemon.pokemon.move_lst[2].name, 200, 440, 300, 450)
            ability4 = button(current_Pokemon.pokemon.move_lst[3].name, 200, 480, 300, 490)
            ability1.show_text(screen, font)
            ability2.show_text(screen, font)
            ability3.show_text(screen, font)
            ability4.show_text(screen, font)
            ab1lst = ability1.coordinates()
            ab2lst = ability2.coordinates()
            ab3lst = ability3.coordinates()
            ab4lst = ability4.coordinates()

            if(active_ability1):
                received_dict = client.battle(current_Pokemon.pokemon, current_Pokemon.pokemon.move_lst[0])
                change(current_Pokemon.pokemon, received_dict['my_pkmn'])
                change(enemy_Pokemon.pokemon, received_dict['op_pkmn'])
            elif(active_ability2):
                received_dict = client.battle(current_Pokemon.pokemon, current_Pokemon.pokemon.move_lst[1])
                change(current_Pokemon.pokemon, received_dict['my_pkmn'])
                change(enemy_Pokemon.pokemon, received_dict['op_pkmn'])
            elif(active_ability3):
                received_dict = client.battle(current_Pokemon.pokemon, current_Pokemon.pokemon.move_lst[2])
                change(current_Pokemon.pokemon, received_dict['my_pkmn'])
                change(enemy_Pokemon.pokemon, received_dict['op_pkmn'])
            elif(active_ability4):
                received_dict = client.battle(current_Pokemon.pokemon, current_Pokemon.pokemon.move_lst[3])
                change(current_Pokemon.pokemon, received_dict['my_pkmn'])
                change(enemy_Pokemon.pokemon, received_dict['op_pkmn'])
            

            #client.battle(pokemon, move) references
            # received_dict = client.battle(pokemon, move)
            # one boolean in dict will control attack order


                
            
            
                
                    
            
             
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
                if check_Bounds(ab1lst) and active_Screen4:
                    active_ability1 = True
                elif check_Bounds(ab2lst) and active_Screen4:
                    active_ability2 = True
                elif check_Bounds(ab3lst) and active_Screen4:
                    active_ability3 = True
                elif check_Bounds(ab4lst) and active_Screen4:
                    active_ability4 = True
                
            
                
                    
                
                
        pygame.display.update()

def check_lst(name, lst):
    return name in lst
def input1(screen, font, name = ''):
    while True:
        for evt in pygame.event.get():
            if evt.type == KEYDOWN:
                if evt.unicode.isalpha():
                    name += evt.unicode
                elif evt.key == K_BACKSPACE:
                    name = name[:-1]
                elif evt.key == K_RETURN:
                    name = ""
                elif evt.key == K_SPACE:
                    return name
            if evt.type == MOUSEBUTTONDOWN:
                break
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

def display_Background(screen, file_abspath):
    background = pygame.transform.scale(pygame.image.load(file_abspath), (SCREENSIZE_X, SCREENSIZE_Y))
    screen.blit(background, (0, 0))

    #pygame.display.update()
    
def draw_box(screen, font,x1,y1,x2,y2,name,level,hp, total_hp):
    display_Image(screen, 'asset\\image\\box.png', x1,y1,x2,y2)
    mts(screen, font, name, (0,0,255), x1 + (x2-x1)//3, y1 + (y2-y1)//3)
    mts(screen, font, "lv " + str(level), (0,0,255),x1 + (x2-x1)//3*2 , y1 + (y2-y1)//3)
    mts(screen, font, "HP: " + str(hp) + "/" + str(total_hp), (0,0,255), x1 + 5, y2 - 50)
    hp_outline = pygame.Rect(x1 + (x2-x1)//3, y1 + (y2 - y1)//3 * 2, int((x2 - x1)//3) + 50, y1 + (y2 - y1)//3 - 5)
    hp_box = pygame.Rect(x1 + (x2-x1)//3, y1 + (y2 - y1)//3 * 2, int(((x2 - x1)//3 + 50) * hp/total_hp), y1 + (y2 - y1)//3 - 5)
    pygame.draw.rect(screen, [0,0,0], hp_outline, 2)
    pygame.draw.rect(screen, [255, 0, 0], hp_box)


def change(pokemon, ls):
    pokemon.name = ls[0]
    pokemon.HP = ls[1]
    pokemon.Attack = ls[2]
    pokemon.Defense = ls[3]
    pokemon.SpAttack = ls[4]
    pokemon.SpDefense = ls[5]
    pokemon.Speed = ls[6]
    pokemon.level = ls[7]
    pokemon.critical = ls[8]
    pokemon.accuracy = ls[9]
    pokemon.evasion = ls[10]
    pokemon.atk_mod = ls[11]
    pokemon.def_mod = ls[12]
    pokemon.spatk_mod = ls[13]
    pokemon.spdef_mod = ls[14]
    pokemon.spd_mod = ls[15]
    pokemon.stat = ls[16]
    pokemon.type = ls[17]
    pokemon.acc_mod = ls[18]
    pokemon.eva_mod = ls[19]

main()
