import pyodbc
db = pyodbc.connect(r'DRIVER={Microsoft Access Driver (*.mdb, *.accdb)};'r'DBQ=C:\Users\13918\Documents\Summer\Pokemon-Battle-Simulation\asset\database\BaseStatus.accdb;').cursor()
db.execute("select Move from Moves where ID < 386")
lst = list(db)
print(lst[-1])
mv_set = {"a"}
mv_set.remove("a")
for item in lst:
    for mv in item[0].split(", "):
        mv_set.add(mv)
print(mv_set)
db.close()