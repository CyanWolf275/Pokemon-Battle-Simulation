import pyodbc
class Move(object):

    def __init__(self, name):
        self.name = name
        db = pyodbc.connect(r'DRIVER={Microsoft Access Driver (*.mdb, *.accdb)};'r'DBQ=C:\Users\13918\Documents\Summer\Pokemon-Battle-Simulation\asset\database\BaseStatus.accdb;')
        cursor = db.cursor()
        cursor.execute("select * from MoveList where Name = '" + self.name + "'")
        lst = list(cursor)
        self.prop = lst[2]
        self.cat = lst[3]
        self.acc = lst[4]
        self.pp = lst[5]
        self.pwr = lst[6]
        self.my_code = lst[7]
        self.op_code = lst[8]
        cursor.close()
        db.close()
    
    def atk(self, pkmn):
        self.pp -= 1
        if self.cat == "Physical":
            return pkmn.Attack
        elif self.cat == "Special":
            return pkmn.SpAttack
        else:
            return 0
    
    