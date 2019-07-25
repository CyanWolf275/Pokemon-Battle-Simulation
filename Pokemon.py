import pyodbc, functions
from Move import Move
from random import shuffle
import os

class Pokemon(object):
    
    #attributes:
    #name
    #Attack
    #Defense
    #SpAttack
    #SpDefence
    #Speed
    #FrontPic
    #BackPic
    #level
    #critical
    #ability
    #client -> server: 0name, 1hp, 2atk, 3def, 4spatk, 5spdef, 6spd, 7lv, 8crt, 9acc, 10eva, 11matk, 12mdef, 13mspatk, 14mspdef, 15mspd, 16stat, 17type
    #0name, 1prop, 2cat, 3acc, 4pp, 5pwr, 6myc, 7opc
    def __init__(self, name):
        db = pyodbc.connect(r'DRIVER={Microsoft Access Driver (*.mdb, *.accdb)};'r'DBQ=BaseStatus.accdb;')
        cursor = db.cursor()
        cursor.execute("select * from BaseStat where EnName = '" + name + "'")
        param_lst = list(cursor)[0]
        self.name = name
        self.level = 50
        self.HP = functions.hp(param_lst[2], 85, self.level)
        self.Attack = functions.other_state(param_lst[3], 85, self.level, 1)
        self.Defense = functions.other_state(param_lst[4], 85, self.level, 1)
        self.SpAttack = functions.other_state(param_lst[5], 85, self.level, 1)
        self.SpDefence = functions.other_state(param_lst[6], 85, self.level, 1)
        self.Speed = functions.other_state(param_lst[7], 85, self.level, 1)
        self.FrontPic = "asset\\image\\pokemon\\" + name + ".png"
        self.BackPIc = "asset\\image\\pokemon\\" + name + "_b.png"
        self.critical = 0
        self.accuracy = 1.0
        self.evasion = 1.0
        self.atk_mod = 1
        self.def_mod = 1
        self.spatk_mod = 1
        self.spdef_mod = 1
        self.spd_mod = 1
        self.stat = "None"
        self.type = param_lst[8]
        cursor.execute("select Move from Moves1 where EnName = '" + self.name + "'")
        available_moves = list(cursor)[0][0].split(", ")
        shuffle(available_moves)
        self.move_lst = [Move(available_moves[0]), Move(available_moves[1]), Move(available_moves[2]), Move(available_moves[3])]
        cursor.close()
        db.close()
    
    def __str__(self):
        return "/".join([self.name, str(self.HP), str(self.Attack), str(self.Defense), str(self.SpAttack), str(self.SpDefence), str(self.Speed), str(self.level), str(self.critical), str(self.accuracy), str(self.evasion), str(self.atk_mod), str(self.def_mod), str(self.spatk_mod), str(self.spdef_mod), str(self.spd_mod), self.stat, self.type])
