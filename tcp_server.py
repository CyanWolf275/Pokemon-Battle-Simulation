import socket, pyodbc, functions
from random import random

class server(object):
    
    def __init__(self, ip, port):
        self.s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.info = (ip, port)
        self.move_db = pyodbc.connect( r'DRIVER={Microsoft Access Driver (*.mdb, *.accdb)};' r'DBQ=C:\Users\jeffr\OneDrive\Desktop\VS2020\BattleSimulation\Pokemon-Battle-Simulation\asset\database\BaseStatus.accdb;').cursor()
        self.s.bind(self.info)
        self.conn = None
    
    def connect(self):
        '''Wait until a connection is established and returns the client's ip address. '''
        self.s.listen(1)
        self.conn, ip = self.s.accept()
        return ip

    def act(self, pkmn, mv):
        '''msg: name, atk_cat, atk, pwr, op_code/miss
        data: hp, status
        '''
        exec(mv.my_code)
        msg = ""
        if random() >= mv.acc:
            msg = "miss"
        else:
            msg = mv.name + ", " + mv.cat + ", " + str(mv.atk(pkmn)) + ", " + mv.pwr + mv.op_code
        self.conn.send(msg)
        data = conn.recv().split(", ")
        return {"hp": data[0], "status": data[1]}

s = server("127.0.0.1", 1000)
print(s.connect())
s.conn.sendall("123")

<<<<<<< HEAD
    def act(self, pkmn, move):
        #self.move_db.execute("select * from Status where EnName = '" + move + "'")
        pass
=======
>>>>>>> 37fb2b96fb541dec85d3ad8c809a9e3ff83b091c
