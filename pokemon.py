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
    def __init__(self,name,Attack,Defense,SpAttack,SpDefence,Speed,FrontPic,BackPic,level,critical,ability):
        self.name = name
        self.HP = HP
        self.Attack = Attack
        self.Defense = Defense
        self.SpAttack = SpAttack
        self.SpDefence = SpDefence
        self.Speed = Speed
        self.FrontPic = FrontPic
        self.BackPIc = BackPic
        self.level = level
        self.critical = critical
        self.accuracy = accuracy
        self.ability = ability
        self.atk_mod = 1
        self.def_mod = 1
        self.spatk_mod = 1
        self.spdef_mod = 1
        self.spd_mod = 1
        self.stat = ""
    
    def __str__(self):
        return " ".join([self.name, self.HP, self.Attack, self.Defense, self.SpAttack, self.SpDefence, self.Speed, self.level, self.critical, self.accuracy, self.evasion, self.atk_mod, self.def_mod, self.spatk_mod, self.spdef_mod, self.spd_mod, self.stat])
