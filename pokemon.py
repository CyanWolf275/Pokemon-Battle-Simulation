import Move
class Pokemon:
    
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
    
    def __init__(self,name,Attack,Defense,SpAttack,SpDefence,Speed,FrontPic,BackPic,level,critical,ability):
        self.name = name
        self.Attack = Attack
        self.Defense = Defense
        self.SpAttack = SpAttack
        self.SpDefence = SpDefence
        self.Speed = Speed
        self.FrontPic = FrontPic
        self.BackPIc = BackPic
        self.level = level
        self.critical = critical
        self.ability = ability
        self.mv1 = Move()
