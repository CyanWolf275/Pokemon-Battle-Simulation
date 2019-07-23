from bs4 import BeautifulSoup
from bs4 import SoupStrainer
import requests, pyodbc
db = pyodbc.connect(r'DRIVER={Microsoft Access Driver (*.mdb, *.accdb)};'r'DBQ=C:\Users\13918\Documents\Summer\Pokemon-Battle-Simulation\asset\database\BaseStatus.accdb;').cursor()
r = requests.get("https://bulbapedia.bulbagarden.net/wiki/Bulbasaur_(Pok%C3%A9mon)/Generation_VI_learnset#By_leveling_up")
soup = BeautifulSoup(r.text, 'html.parser')
trs = soup.findall("tr")
