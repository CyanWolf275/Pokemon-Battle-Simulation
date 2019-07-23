import re, requests, shutil, pyodbc

def func(num):
    num = str(num)
    if len(num) == 1:
        return "00" + num
    elif len(num) == 2:
        return "0" + num
    else:
        return num

db = pyodbc.connect(r'DRIVER={Microsoft Access Driver (*.mdb, *.accdb)};'r'DBQ=C:\Users\13918\Documents\Summer\Pokemon-Battle-Simulation\asset\database\BaseStatus.accdb;')
cursor = db.cursor()
cursor.execute("select EnName from BaseStat")
pkmn = cursor.fetchall()
i = 1
for p in pkmn:
    name = str(p[0])
    lnk1 = requests.get("https://bulbapedia.bulbagarden.net/wiki/" + name + "_(Pok%C3%A9mon)")
    lnk2 = requests.get("https://bulbapedia.bulbagarden.net/wiki/" + name + "_(Pok%C3%A9mon)")
    url1 = "http://" + re.findall(r'cdn\.bulbagarden\.net\/upload.*?Spr_6x_.*?\.png', lnk1.text)[0]
    url2 = "http://" + re.findall(r'cdn\.bulbagarden\.net\/upload.*?Spr_b_6x_.*?\.png', lnk2.text)[0]
    r1 = requests.get(url1, stream = True)
    r2 = requests.get(url2, stream = True)
    with open("C:\\Users\\13918\\Documents\\Summer\\Pokemon-Battle-Simulation\\asset\\image\\pokemon\\" + name + ".png", 'wb') as f1:
        r1.raw.decode_content = True
        shutil.copyfileobj(r1.raw, f1)
    with open("C:\\Users\\13918\\Documents\\Summer\\Pokemon-Battle-Simulation\\asset\\image\\pokemon\\" + name + "_b.png", 'wb') as f2:
        r2.raw.decode_content = True
        shutil.copyfileobj(r2.raw, f2)
    print(i)
    i += 1
cursor.close()
db.close()