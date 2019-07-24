from bs4 import BeautifulSoup
import requests, pyodbc
db = pyodbc.connect(r'DRIVER={Microsoft Access Driver (*.mdb, *.accdb)};'r'DBQ=C:\Users\13918\Documents\Summer\Pokemon-Battle-Simulation\asset\database\BaseStatus.accdb;')
cursor = db.cursor()
cursor.execute("select EnName from Moves1")
pkmn = cursor.fetchall()
i = 1
for p in pkmn:
    try:
        r = requests.get("https://pokemondb.net/pokedex/" + str(p[0]).lower() + "/moves/1")
        soup = BeautifulSoup(r.text, 'html.parser')
        tab = soup.find_all("table")[0]
        table = tab.find_all("tr")
        lst = {"a"}
        lst.remove("a")
        for row in table:
            cells = row.find_all("td")
            if len(cells) >= 2:
                lst.add(cells[1].get_text())
        output = ""
        for item in lst:
            output += item + ", "
        cursor.execute("update Moves1 set Move = '" + output[:-2] + "' where EnName = '" + str(p[0]) + "'")
        db.commit()
        print(i)
        i += 1
    except:
        print(str(p[0]) + "omitted " + str(i))
        i += 1
cursor.close()
db.close()