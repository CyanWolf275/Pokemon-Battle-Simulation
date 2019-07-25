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
    #client -> server: name, hp, atk, def, spatk, spdef, spd, lv, crt, acc, eva, matk, mdef, mspatk, mspdef, mspd, stat
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
