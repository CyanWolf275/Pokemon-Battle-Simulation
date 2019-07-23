from bs4 import BeautifulSoup
import requests, pyodbc
db = pyodbc.connect(r'DRIVER={Microsoft Access Driver (*.mdb, *.accdb)};'r'DBQ=C:\Users\13918\Documents\Summer\Pokemon-Battle-Simulation\asset\database\BaseStatus.accdb;')
cursor = db.cursor()
cursor.execute("select EnName from BaseStat")
pkmn = cursor.fetchall()
i = 1
for p in pkmn:
    r = requests.get("https://pokemondb.net/pokedex/" + str(p[0]).lower())
    soup = BeautifulSoup(r.text, 'html.parser')
    tab = soup.find_all("table")[0]
    table = tab.find_all("tr")
    lst = table[1].find_all("td")[0].get_text()
    cursor.execute("update BaseStat set Type = '" + lst[1:-1] + "' where EnName = '" + str(p[0]) + "'")
    db.commit()
    print(i)
    i += 1
cursor.close()
db.close()