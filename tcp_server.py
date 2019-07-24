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
        lst1 = self.recv1.split(" ")
        lst2 = self.recv2.split(" ")
    
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