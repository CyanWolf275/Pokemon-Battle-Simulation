import random, pyodbc


def hp(base,ev,level):
    hp = ((2 * base + 31 + ev/4) * level)/100 + level + 10
    return int(hp)

def other_state(base,ev,level,nature):
    other_state = (((2 * base + 31 + ev/4) * level)/100 + 5) * nature
    return int(other_state)

def damage(level,power,attack,defense,modifier):
    damage = (((2 * level / 5 + 2) * power * attack / defense/50) + 2) * modifier
    return int(damage)

def modifier(weather,Type,critical_hit,p_type,m_type,adaptability,o_type,burn):
    
    #critical_hit: whether the hit is a critical hit
    #match: if the move's type matches any of the user's types
    #adaptability: whether the user has adaptability
    #type_effectiveness: int
    
    
    weather_num = 1
    critical_num = critical_hit(critical_hit)
    random_num = random.randint(85,100)/100
    stab_num = STAB(p_type,m_type,adaptability)
    type_num = cal_type(p_type, o_type)
    burn_num = burn(burn)
    
    return weather_num * critical_num * random_num * stab_num * type_num * burn_num
    

def weather(weather,Type):
    
    if Type == "water" and weather == "rain":
        return 1.5
    elif Type == "fire" and weather == "sunlight":
        return 1.5
    elif Type == "water" and weather == "sunlight":
        return 0.5
    elif Type == "fire" and weather == "rain":
        return 0.5
    else:
        return 1
    
def critical_hit(critical):
    if critical == 0:
        num = random.randint(1,100)
        if num < 6.25:
            temp = True
        else:
            temp = False
            
    if critical == 1:
        num = random.randint(1,100)
        if num < 12.5:
            temp = True
        else:
            temp = False
    
    if critical == 2:
        num = random.randint(1,100)
        if num < 50:
            temp = True
        else:
            temp = False
            
    if critical >= 3:
        temp = True

    if temp:
        return 2
    else:
        return 1
    
def STAB(p_type,m_type,adaptability):
    if m_type in p_type and adaptability:
        return 2
    elif m_type in p_type:
        return 1.5
    else:
        return 1
        
def burn(burn):
    if burn:
        return 0.5
    else:
        return 1
    
def number(num):
    num = str(num)
    if len(num) == 1:
        return "00" + num
    elif len(num) == 2:
        return "0" + num
    else:
        return num

def cal_type(atk, dfc):
    db = pyodbc.connect(r'DRIVER={Microsoft Access Driver (*.mdb, *.accdb)};'r'DBQ=asset\database\Types.accdb;')
    cursor = db.cursor()
    cursor.execute("select " + atk[:3] + " from " + dfc.split(" ")[0] + " where Type = '" + dfc + "'")
    result = float(cursor.fetchone()[0])
    cursor.close()
    db.close()
    return result

def stage(val, st):
    '''returns the actual value under the effect of stage (-6 - +6)'''
    stage = [-6,-5,-4,-3,-2,-1,0,1,2,3,4,5,6]
    multiplier = [2/8,2/7,2/6,2/5,2/4,2/3,2/2,3/2,4/2,5/2,6/2,7/2,8/2]
    for x in range(0,len(stage)):
        if stage[x] == st:
            return int(val * multiplier[x])

def poke_lst():
    db = pyodbc.connect(r'DRIVER={Microsoft Access Driver (*.mdb, *.accdb)};'r'DBQ=./BaseStatus.accdb;')
    cursor = db.cursor()
    cursor.execute("select EnName from BaseStat where ID < 152")
    result = [item[0] for item in list(cursor)]
    cursor.close()
    db.close()
    return result

def change(pokemon,ls):
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
