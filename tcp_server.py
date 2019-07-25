import socket, pyodbc, functions, time, threading, multiprocessing
from random import random

class server(object):
    
    def __init__(self, ip, port):
        self.s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        self.info = (ip, port)
        #self.move_db = pyodbc.connect( r'DRIVER={Microsoft Access Driver (*.mdb, *.accdb)};' r'DBQ=C:\Users\jeffr\OneDrive\Desktop\VS2020\BattleSimulation\Pokemon-Battle-Simulation\asset\database\BaseStatus.accdb;').cursor()
        self.s.bind(self.info)
        self.recv1 = ""
        self.recv2 = ""
    
    def connect(self):
        '''Wait until a connection is established and returns the client's ip address. '''
        self.s.listen(128)
        self.conn1, ip1 = self.s.accept()
        self.conn2, ip2 = self.s.accept()
        return ip1, ip2

    def receive1(self):
        while True:
            self.recv1 = self.conn1.recv(1024).decode()
            print("received " + self.recv1)
    
    def receive2(self):
        while True:
            self.recv2 = self.conn2.recv(1024).decode()
            print("received " + self.recv2)
    
    def press_start(self):
        while not self.recv1 == "start" or not self.recv2 == "start":
            time.sleep(0.1)
        self.conn1.send(b'start')
        self.conn2.send(b'start')
        self.recv1 = ""
        self.recv2 = ""
    
    def round(self):
        while self.recv1 == "" or self.recv2 == "":
            time.sleep(0.1)
        lst1 = self.recv1.split(", ")
        pkmn1 = lst1[0].split("/")
        mv1 = lst1[1].split("/")
        lst2 = self.recv2.split(", ")
        pkmn2 = lst2[0].split("/")
        mv2 = lst2[1].split("/")
        dmg1 = 0
        dmg2 = 0
        one_first = True
        if functions.stage(int(pkmn1[6]), int(pkmn1[15])) > functions.stage(int(pkmn2[6]), int(pkmn2[15])):
            one_first = True
            if mv1[2] == "Physical":
                if mv2[2] == "Physical":
                    dmg1 = functions.damage(int(pkmn1[7]), int(mv1[5]), functions.stage(int(pkmn1[2]), int(pkmn1[11])), functions.stage(int(pkmn2[3]), int(pkmn2[12])), functions.modifier("", "", int(pkmn1[8]), pkmn1[17], mv1[1], False, pkmn2[17], False))
                    exec(mv1[6])
                    exec(mv1[7])
                    dmg2 = functions.damage(int(pkmn2[7]), int(mv2[5]), functions.stage(int(pkmn2[2]), int(pkmn2[11])), functions.stage(int(pkmn1[3]), int(pkmn1[12])), functions.modifier("", "", int(pkmn2[8]), pkmn2[17], mv2[1], False, pkmn1[17], False))
                    exec(mv2[6])
                    exec(mv2[7])
                else:
                    dmg1 = functions.damage(int(pkmn1[7]), int(mv1[5]), functions.stage(int(pkmn1[2]), int(pkmn1[11])), functions.stage(int(pkmn2[3]), int(pkmn2[12])), functions.modifier("", "", int(pkmn1[8]), pkmn1[17], mv1[1], False, pkmn2[17], False))
                    exec(mv1[6])
                    exec(mv1[7])
                    dmg2 = functions.damage(int(pkmn2[7]), int(mv2[5]), functions.stage(int(pkmn2[4]), int(pkmn2[13])), functions.stage(int(pkmn1[5]), int(pkmn1[14])), functions.modifier("", "", int(pkmn2[8]), pkmn2[17], mv2[1], False, pkmn1[17], False))
                    exec(mv2[6])
                    exec(mv2[7])
            else:
                if mv2[2] == "Physical":
                    dmg1 = functions.damage(int(pkmn1[7]), int(mv1[5]), functions.stage(int(pkmn1[4]), int(pkmn1[13])), functions.stage(int(pkmn2[5]), int(pkmn2[14])), functions.modifier("", "", int(pkmn1[8]), pkmn1[17], mv1[1], False, pkmn2[17], False))
                    exec(mv1[6])
                    exec(mv1[7])
                    dmg2 = functions.damage(int(pkmn2[7]), int(mv2[5]), functions.stage(int(pkmn2[2]), int(pkmn2[11])), functions.stage(int(pkmn1[3]), int(pkmn1[12])), functions.modifier("", "", int(pkmn2[8]), pkmn2[17], mv2[1], False, pkmn1[17], False))
                    exec(mv2[6])
                    exec(mv2[7])
                else:
                    dmg1 = functions.damage(int(pkmn1[7]), int(mv1[5]), functions.stage(int(pkmn1[4]), int(pkmn1[13])), functions.stage(int(pkmn2[5]), int(pkmn2[14])), functions.modifier("", "", int(pkmn1[8]), pkmn1[17], mv1[1], False, pkmn2[17], False))
                    exec(mv1[6])
                    exec(mv1[7])
                    dmg2 = functions.damage(int(pkmn2[7]), int(mv2[5]), functions.stage(int(pkmn2[4]), int(pkmn2[13])), functions.stage(int(pkmn1[5]), int(pkmn1[14])), functions.modifier("", "", int(pkmn2[8]), pkmn2[17], mv2[1], False, pkmn1[17], False))
                    exec(mv2[6])
                    exec(mv2[7])
        else:
            one_first = False
            if mv2[2] == "Physical":
                if mv1[2] == "Physical":
                    dmg2 = functions.damage(int(pkmn2[7]), int(mv2[5]), functions.stage(int(pkmn2[2]), int(pkmn2[11])), functions.stage(int(pkmn1[3]), int(pkmn1[12])), functions.modifier("", "", int(pkmn2[8]), pkmn2[17], mv2[1], False, pkmn1[17], False))
                    exec(mv2[6])
                    exec(mv2[7])
                    dmg1 = functions.damage(int(pkmn1[7]), int(mv1[5]), functions.stage(int(pkmn1[2]), int(pkmn1[11])), functions.stage(int(pkmn2[3]), int(pkmn2[12])), functions.modifier("", "", int(pkmn1[8]), pkmn1[17], mv1[1], False, pkmn2[17], False))
                    exec(mv1[6])
                    exec(mv1[7])
                else:
                    dmg2 = functions.damage(int(pkmn2[7]), int(mv2[5]), functions.stage(int(pkmn2[2]), int(pkmn2[11])), functions.stage(int(pkmn1[3]), int(pkmn1[12])), functions.modifier("", "", int(pkmn2[8]), pkmn2[17], mv2[1], False, pkmn1[17], False))
                    exec(mv2[6])
                    exec(mv2[7])
                    dmg1 = functions.damage(int(pkmn1[7]), int(mv1[5]), functions.stage(int(pkmn1[4]), int(pkmn1[13])), functions.stage(int(pkmn2[5]), int(pkmn2[14])), functions.modifier("", "", int(pkmn1[8]), pkmn1[17], mv1[1], False, pkmn2[17], False))
                    exec(mv1[6])
                    exec(mv1[7])
            else:
                if mv1[2] == "Physical":
                    dmg2 = functions.damage(int(pkmn2[7]), int(mv2[5]), functions.stage(int(pkmn2[4]), int(pkmn2[13])), functions.stage(int(pkmn1[5]), int(pkmn1[14])), functions.modifier("", "", int(pkmn2[8]), pkmn2[17], mv2[1], False, pkmn1[17], False))
                    exec(mv2[6])
                    exec(mv2[7])
                    dmg1 = functions.damage(int(pkmn1[7]), int(mv1[5]), functions.stage(int(pkmn1[2]), int(pkmn1[11])), functions.stage(int(pkmn2[3]), int(pkmn2[12])), functions.modifier("", "", int(pkmn1[8]), pkmn1[17], mv1[1], False, pkmn2[17], False))
                    exec(mv1[6])
                    exec(mv1[7])
                else:
                    dmg2 = functions.damage(int(pkmn2[7]), int(mv2[5]), functions.stage(int(pkmn2[4]), int(pkmn2[13])), functions.stage(int(pkmn1[5]), int(pkmn1[14])), functions.modifier("", "", int(pkmn2[8]), pkmn2[17], mv2[1], False, pkmn1[17], False))
                    exec(mv2[6])
                    exec(mv2[7])
                    dmg1 = functions.damage(int(pkmn1[7]), int(mv1[5]), functions.stage(int(pkmn1[4]), int(pkmn1[13])), functions.stage(int(pkmn2[5]), int(pkmn2[14])), functions.modifier("", "", int(pkmn1[8]), pkmn1[17], mv1[1], False, pkmn2[17], False))
                    exec(mv1[6])
                    exec(mv1[7])
        pkmn2[1] -= dmg1
        pkmn1[1] -= dmg2
        self.conn1.send(("/".join(pkmn2) + ", " + "/".join(pkmn1) + ", " + str(one_first)).encode())
        self.conn2.send(("/".join(pkmn1) + ", " + "/".join(pkmn2) + ", " + str(not one_first)).encode())
        self.recv1 = ""
        self.recv2 = ""
    
def main():
    s = server("", 7788)
    client = s.connect()
    print("Client 1: " + str(client[0]))
    print("Client 2: " + str(client[1]))
    p1 = threading.Thread(target = s.receive1)
    p2 = threading.Thread(target = s.receive2)
    p1.start()
    p2.start()
    s.press_start()
    print("GAME START")
    s.round()
    s.s.close()

main()
