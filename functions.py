import random

def hp(base,IV,ev,level):
    hp = (2 * base + IV + ev/4 * level)/100 + level + 10
    return int(hp)

def other_state(base,IV,ev,level,nature):
    other_state = ((2 * base + IV + ev/4 * level)/100 + 5) * nature
    return int(other_state)

def damage(level,power,attack,defense,modifier):
    damage = (((2 * level / 5 + 2) * power * attack / defense/50) + 2) * modifier
    return int(damage)

def modifier(weather,Type,critical_hit,match,adaptability,type_effectiveness,burn):
    
    #critical_hit: whether the hit is a critical hit
    #match: if the move's type matches any of the user's types
    #adaptability: whether the user has adaptability
    #type_effectiveness: int
    
    
    weather_num = weather(weather,Type)
    critical_num = critical_hit(critical_hit)
    random_num = random.randint(85,100)/100
    stab_num = STAB(match,adaptability)
    type_num = type_effectiveness
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
    if critical:
        return 2
    else:
        return 1
    
def STAB(match,adaptability):
    if match and adaptability:
        return 2
    elif match:
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
